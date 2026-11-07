# Лабораторная работа № 2
# Блок 3. Комбинаторы

# Задание 3.1. Базовые комбинаторы I, K, S, B, C

def I(x):
    return x


def K(x):
    return lambda y: x


def S(f):
    return lambda g: lambda x: f(x)(g(x))


def B(f):
    return lambda g: lambda x: f(g(x))


def C(f):
    return lambda x: lambda y: f(y)(x)


def inc(x):
    return x + 1


def double(x):
    return x * 2


print("Задание 3.1")
print("I(5):", I(5))
print("K('a')('b'):", K("a")("b"))
print("S(K)(K)(7):", S(K)(K)(7))
print("B(inc)(double)(5):", B(inc)(double)(5))
print("inc(double(5)):", inc(double(5)))
print("C(K)('a')('b'):", C(K)("a")("b"))
print("K a b -> a:", K("a")("b") == "a")
print("S K K x -> x:", S(K)(K)(7) == 7)
print("B f g x -> f(g(x)):", B(inc)(double)(5) == inc(double(5)))


# Задание 3.2. SK-базис
# B = S (K S) K

B_from_SK = S(K(S))(K)

print("\nЗадание 3.2")
print("Редукция S K K x -> K x (K x) -> x")
for x in [2, 5, 10]:
    print("x =", x, "| S K K x =", S(K)(K)(x), "| I x =", I(x))

print("B через S и K:", B_from_SK(inc)(double)(5))
print("Обычный B:", B(inc)(double)(5))
print("Результаты совпадают:", B_from_SK(inc)(double)(5) == B(inc)(double)(5))


# Задание 3.3. Y-комбинатор и рекурсия
# Для Python используется вариант с отложенным рекурсивным вызовом.
# Он соответствует Z-комбинатору для жадного порядка вычислений.

def Y(f):
    def helper(x):
        return f(lambda n: x(x)(n))
    return helper(helper)


def factorial_body(rec):
    def calculate(n):
        if n == 0:
            return 1
        return n * rec(n - 1)
    return calculate


def fibonacci_body(rec):
    def calculate(n):
        if n < 2:
            return n
        return rec(n - 1) + rec(n - 2)
    return calculate


def sum_body(rec):
    def calculate(numbers):
        if not numbers:
            return 0
        return numbers[0] + rec(numbers[1:])
    return calculate


factorial = Y(factorial_body)
fibonacci = Y(fibonacci_body)
sum_list = Y(sum_body)

print("\nЗадание 3.3")
print("Факториал 5:", factorial(5))
print("Фибоначчи 7:", fibonacci(7))
print("Сумма [1, 2, 3, 4, 5]:", sum_list([1, 2, 3, 4, 5]))

# Проверяем Y(f) и f(Y(f)) на одинаковых аргументах.
print("Свойство Y f = f(Y f) для факториала:",
      factorial(5) == factorial_body(factorial)(5))
print("Свойство Y f = f(Y f) для Фибоначчи:",
      fibonacci(7) == fibonacci_body(fibonacci)(7))
print("Свойство Y f = f(Y f) для суммы:",
      sum_list([1, 2, 3]) == sum_body(sum_list)([1, 2, 3]))


# Задание 3.4. Числа Чёрча (дополнительное)

def zero(f):
    return lambda x: x


def succ(n):
    return lambda f: lambda x: f(n(f)(x))


def plus(m):
    return lambda n: lambda f: lambda x: m(f)(n(f)(x))


def mult(m):
    return lambda n: lambda f: lambda x: m(n(f))(x)


def to_int(n):
    return n(lambda x: x + 1)(0)


one = succ(zero)
two = succ(one)
three = succ(two)

print("\nЗадание 3.4 (дополнительное)")
print("Число zero:", to_int(zero))
print("Число two:", to_int(two))
print("Число three:", to_int(three))
print("plus 2 3:", to_int(plus(two)(three)))
print("mult 2 3:", to_int(mult(two)(three)))
print("2 + 3 = 5:", to_int(plus(two)(three)) == 5)
print("2 * 3 = 6:", to_int(mult(two)(three)) == 6)
