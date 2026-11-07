# Лабораторная работа № 3
# Блок 3. Каррирование и частичное применение
# Вариант 17 — «Курьерская служба»

from functools import partial


# Задание 3.1
# Обычная и каррированная функции сложения и вычитания

def add(a, b):
    return a + b


def add_curried(a):
    def with_b(b):
        return a + b
    return with_b


def subtract(a, b):
    return a - b


def subtract_curried(a):
    def with_b(b):
        return a - b
    return with_b


add5 = add_curried(5)
subtract_from_10 = subtract_curried(10)

print("Задание 3.1")
checks_3_1 = [
    (add(5, 8), add_curried(5)(8), 13),
    (add5(2), add(5, 2), 7),
    (subtract_from_10(3), subtract(10, 3), 7),
    (subtract_from_10(12), subtract(10, 12), -2),
    (subtract_from_10(0), subtract(10, 0), 10),
    (subtract_curried(-2)(3), subtract(-2, 3), -5),
]
for ordinary, curried, expected in checks_3_1:
    assert ordinary == curried == expected
    print(f"Обычная: {ordinary}, каррированная: {curried}")

# Каррирование: сначала передаём первый аргумент, затем второй.
# При вызове subtract_curried(10) сохраняется значение первого аргумента.


# Задание 3.2
# Частичное применение с functools.partial

def cost(rate, base, count):
    return rate * count + base


standard = partial(cost, 20, 100)
second_tariff = partial(cost, 30, 50)
only_rate = partial(cost, 20)

print("\nЗадание 3.2")
checks_3_2 = [
    ("Стандарт, 3 шт.", standard(3), cost(20, 100, 3), 160),
    ("Стандарт, 0 шт.", standard(0), cost(20, 100, 0), 100),
    ("Второй тариф, 3 шт.", second_tariff(3), cost(30, 50, 3), 140),
    ("Второй тариф, 0 шт.", second_tariff(0), cost(30, 50, 0), 50),
    ("Только rate, base=10", only_rate(10, 3), cost(20, 10, 3), 70),
    ("Только rate, base=0", only_rate(0, 4), cost(20, 0, 4), 80),
]
for name, result, ordinary, expected in checks_3_2:
    assert result == ordinary == expected
    print(f"{name}: {result} (обычный вызов: {ordinary})")

# partial фиксирует готовые аргументы функции cost.
# Функция cost не превращается в цепочку функций одного аргумента.


# Задание 3.3
# Обычная и каррированная формы affine(a, b, x) = a * x + b

def affine(a, b, x):
    return a * x + b


def affine_curried(a):
    def with_b(b):
        def with_x(x):
            return a * x + b
        return with_x
    return with_b


affine_ready = affine_curried(2)(3)

print("\nЗадание 3.3")
checks_3_3 = [
    (2, 3, 5, 13),
    (0, 4, 8, 4),
    (3, 0, -2, -6),
    (-2, 5, 3, -1),
    (4, -3, 0, -3),
]
for a, b, x, expected in checks_3_3:
    ordinary = affine(a, b, x)
    curried = affine_curried(a)(b)(x)
    assert ordinary == curried == expected
    print(f"a={a}, b={b}, x={x}: {ordinary} == {curried}")
assert affine_ready(5) == 13
print("Функция после фиксации a=2, b=3, x=5 ->", affine_ready(5))


# Задание 3.4
# Фиксация prefix и затем prefix вместе с suffix

def format_message(prefix, suffix, value):
    return prefix + str(value) + suffix


only_prefix = partial(format_message, "Заказ № ")
prefix_and_suffix = partial(format_message, "Заказ № ", "!")

print("\nЗадание 3.4")
checks_3_4 = [
    ("Только prefix, число", only_prefix(".", 17), "Заказ № 17."),
    ("Только prefix, строка", only_prefix(" готов", "А12"), "Заказ № А12 готов"),
    ("Prefix и suffix, число", prefix_and_suffix(17), "Заказ № 17!"),
    ("Prefix и suffix, ноль", prefix_and_suffix(0), "Заказ № 0!"),
    ("Prefix и suffix, строка", prefix_and_suffix("Б4"), "Заказ № Б4!"),
]
for name, result, expected in checks_3_4:
    assert result == expected
    print(f"{name}: {result}")

# В only_prefix остаются два аргумента: suffix и value.
# В prefix_and_suffix остаётся только value.


# Задание 3.5 — вариант 17
# F(a, b, x) = a * x + b ** 2

def formula(a, b, x):
    return a * x + b ** 2


def formula_curried(a):
    def with_b(b):
        def with_x(x):
            return a * x + b ** 2
        return with_x
    return with_b


formula_17 = formula_curried(4)(20)

print("\nЗадание 3.5 — вариант 17")
checks_3_5 = [
    (4, 20, 0, 400),
    (4, 20, 3, 412),
    (4, 20, -2, 392),
    (0, 5, 7, 25),
    (-2, -3, 4, 1),
    (3, 0, -5, -15),
]
for a, b, x, expected in checks_3_5:
    ordinary = formula(a, b, x)
    curried = formula_curried(a)(b)(x)
    assert ordinary == curried == expected
    print(f"F({a}, {b}, {x}): обычная={ordinary}, каррированная={curried}")

for x, expected in [(0, 400), (1, 404), (5, 420), (-5, 380)]:
    assert formula_17(x) == expected
    print(f"Фиксированы a=4, b=20: x={x} -> {formula_17(x)}")


# Задание 3.6 — вариант 17
# C(rate, base, n) = rate * (n + 2) + base

def courier_cost(rate, base, n):
    return rate * (n + 2) + base


courier_first = partial(courier_cost, 4, 20)
courier_second = partial(courier_cost, 6, 25)

print("\nЗадание 3.6 — вариант 17")
checks_3_6 = [
    (0, 28, 37),
    (1, 32, 43),
    (2, 36, 49),
    (5, 48, 67),
    (10, 68, 97),
]
for n, expected_first, expected_second in checks_3_6:
    first = courier_first(n)
    second = courier_second(n)
    assert first == courier_cost(4, 20, n) == expected_first
    assert second == courier_cost(6, 25, n) == expected_second
    print(f"n={n}: тариф (4, 20) -> {first}; тариф (6, 25) -> {second}")

print("\nВсе проверки блока 3 пройдены.")
