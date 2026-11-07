import re


# Задание 2.1. Представление и чтение лямбда-термов

def Var(name):
    return ("var", name)


def Lam(name, body):
    return ("lam", name, body)


def App(f, x):
    return ("app", f, x)


def pretty(t):
    if t[0] == "var":
        return t[1]
    if t[0] == "lam":
        return "\\" + t[1] + ". " + pretty(t[2])

    left = pretty(t[1])
    right = pretty(t[2])
    if t[1][0] == "lam":
        left = "(" + left + ")"
    if t[2][0] != "var":
        right = "(" + right + ")"
    return left + " " + right


def parse(text):
    tokens = re.findall(r"\\|λ|[().]|[^\s\\λ().]+", text)
    pos = 0

    def term():
        nonlocal pos
        if pos < len(tokens) and tokens[pos] in ("\\", "λ"):
            pos += 1
            if pos >= len(tokens):
                raise ValueError("Нет имени переменной")
            name = tokens[pos]
            pos += 1
            if pos >= len(tokens) or tokens[pos] != ".":
                raise ValueError("После имени нужна точка")
            pos += 1
            return Lam(name, term())

        result = atom()
        while pos < len(tokens) and tokens[pos] != ")":
            if tokens[pos] in ("\\", "λ"):
                raise ValueError("Нужны скобки вокруг вложенной функции")
            result = App(result, atom())
        return result

    def atom():
        nonlocal pos
        if pos >= len(tokens):
            raise ValueError("Неожиданный конец выражения")
        if tokens[pos] == "(":
            pos += 1
            result = term()
            if pos >= len(tokens) or tokens[pos] != ")":
                raise ValueError("Не хватает закрывающей скобки")
            pos += 1
            return result
        if tokens[pos] in (".", ")", "\\", "λ"):
            raise ValueError("Неожиданный символ: " + tokens[pos])
        name = tokens[pos]
        pos += 1
        return Var(name)

    if not tokens:
        raise ValueError("Пустой терм")
    result = term()
    if pos != len(tokens):
        raise ValueError("Лишние символы в выражении")
    return result


print("Задание 2.1")
print("Первый терм:", pretty(parse("\\x. x")))
print("Второй терм:", pretty(parse("(\\f. \\x. f (f x))")))


# Задание 2.2. Свободные и связанные переменные

def free_vars(t):
    if t[0] == "var":
        return {t[1]}
    if t[0] == "lam":
        return free_vars(t[2]) - {t[1]}
    return free_vars(t[1]) | free_vars(t[2])


def bound_vars(t):
    if t[0] == "var":
        return set()
    if t[0] == "lam":
        return {t[1]} | bound_vars(t[2])
    return bound_vars(t[1]) | bound_vars(t[2])


print("\nЗадание 2.2")
for text in ["\\x. x y", "\\x. \\y. x y z", "(\\x. x) x"]:
    t = parse(text)
    print(pretty(t))
    print("  Свободные:", sorted(free_vars(t)))
    print("  Связанные:", sorted(bound_vars(t)))


# Задание 2.3. Альфа-эквивалентность

def alpha_eq(a, b, names_a=(), names_b=()):
    if a[0] != b[0]:
        return False
    if a[0] == "var":
        if a[1] in names_a:
            return (b[1] in names_b and
                    names_a[::-1].index(a[1]) == names_b[::-1].index(b[1]))
        return b[1] not in names_b and a[1] == b[1]
    if a[0] == "lam":
        return alpha_eq(a[2], b[2], names_a + (a[1],), names_b + (b[1],))
    return (alpha_eq(a[1], b[1], names_a, names_b) and
            alpha_eq(a[2], b[2], names_a, names_b))


print("\nЗадание 2.3")
checks = [
    ("\\x. x", "\\y. y"),
    ("\\x. \\y. x", "\\a. \\b. a"),
    ("\\x. x y", "\\x. x z")
]
for left, right in checks:
    print(pretty(parse(left)), "и", pretty(parse(right)), "->",
          alpha_eq(parse(left), parse(right)))


# Задание 2.4. Подстановка и бета-редукция

def fresh_name(name, used):
    number = 1
    new_name = name + "_" + str(number)
    while new_name in used:
        number += 1
        new_name = name + "_" + str(number)
    return new_name


def subst(t, x, s):
    if t[0] == "var":
        return s if t[1] == x else t
    if t[0] == "app":
        return App(subst(t[1], x, s), subst(t[2], x, s))

    name, body = t[1], t[2]
    if name == x or x not in free_vars(body):
        return t
    if name in free_vars(s):
        used = free_vars(body) | bound_vars(body) | free_vars(s) | {x, name}
        new_name = fresh_name(name, used)
        body = subst(body, name, Var(new_name))
        name = new_name
    return Lam(name, subst(body, x, s))


def beta_step_normal(t):
    if t[0] == "var":
        return None
    if t[0] == "lam":
        body = beta_step_normal(t[2])
        return Lam(t[1], body) if body is not None else None

    f, x = t[1], t[2]
    if f[0] == "lam":
        return subst(f[2], f[1], x)
    new_f = beta_step_normal(f)
    if new_f is not None:
        return App(new_f, x)
    new_x = beta_step_normal(x)
    return App(f, new_x) if new_x is not None else None


def beta_step_applicative(t):
    if t[0] == "var":
        return None
    if t[0] == "lam":
        body = beta_step_applicative(t[2])
        return Lam(t[1], body) if body is not None else None

    f, x = t[1], t[2]
    new_f = beta_step_applicative(f)
    if new_f is not None:
        return App(new_f, x)
    new_x = beta_step_applicative(x)
    if new_x is not None:
        return App(f, new_x)
    if f[0] == "lam":
        return subst(f[2], f[1], x)
    return None


capture = parse("(\\x. \\y. x) y")
print("\nЗадание 2.4")
print("До подстановки:", pretty(capture))
print("После бета-редукции:", pretty(beta_step_normal(capture)))


# Задание 2.5. Эта-преобразование

def eta_step(t):
    if t[0] == "var":
        return None
    if t[0] == "lam":
        body = t[2]
        if (body[0] == "app" and body[2] == Var(t[1]) and
                t[1] not in free_vars(body[1])):
            return body[1]
        new_body = eta_step(body)
        return Lam(t[1], new_body) if new_body is not None else None

    new_f = eta_step(t[1])
    if new_f is not None:
        return App(new_f, t[2])
    new_x = eta_step(t[2])
    return App(t[1], new_x) if new_x is not None else None


def eta_reduce(t):
    result = eta_step(t)
    return result if result is not None else t


def eta_expand(t):
    used = free_vars(t) | bound_vars(t)
    name = fresh_name("x", used)
    return Lam(name, App(t, Var(name)))


eta_example = parse("\\x. (+ 1) x")
eta_result = eta_reduce(eta_example)
print("\nЗадание 2.5")
print("Исходный терм:", pretty(eta_example))
print("После эта-редукции:", pretty(eta_result))
print("После эта-расширения:", pretty(eta_expand(eta_result)))
print("Расширение снова сокращается:",
      eta_reduce(eta_expand(eta_result)) == eta_result)


# Задание 2.6. Нормальная форма и стратегии

def is_normal(t):
    if t[0] == "var":
        return True
    if t[0] == "lam":
        body = t[2]
        if (body[0] == "app" and body[2] == Var(t[1]) and
                t[1] not in free_vars(body[1])):
            return False
        return is_normal(body)
    if t[1][0] == "lam":
        return False
    return is_normal(t[1]) and is_normal(t[2])


def normalize(t, strategy="normal", limit=1000):
    if strategy not in ("normal", "applicative"):
        raise ValueError("Неизвестная стратегия")

    current = t
    for step in range(limit):
        if strategy == "normal":
            new_t = beta_step_normal(current)
        else:
            new_t = beta_step_applicative(current)
        if new_t is None:
            new_t = eta_step(current)
        if new_t is None:
            return current, step, True
        current = new_t
    return current, limit, is_normal(current)


identity = parse("(\\x. x) y")
omega = parse("(\\x. x x) (\\x. x x)")
different = App(parse("\\x. \\y. y"), omega)

print("\nЗадание 2.6")
print("(\\x. x) y ->", pretty(normalize(identity)[0]))
print("Это нормальная форма:", is_normal(normalize(identity)[0]))

result, steps, finished = normalize(omega, limit=15)
print("Омега: шагов", steps, "нормальная форма найдена:", finished)

result, steps, finished = normalize(different, "normal", 15)
print("Нормальная стратегия:", pretty(result), "; завершена:", finished)

result, steps, finished = normalize(different, "applicative", 15)
print("Аппликативная стратегия: шагов", steps, "; завершена:", finished)
