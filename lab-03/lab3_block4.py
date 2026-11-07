# Лабораторная работа № 3
# Блок 4. Продолжения и CPS-преобразование
# Вариант 17 — «Курьерская служба»

from math import isclose


# Задание 4.1
# Квадрат числа: обычная функция и функция с продолжением

def square(x):
    return x * x


def square_cps(x, k):
    return k(x * x)


print("Задание 4.1")
checks_4_1 = [
    ("Без изменений", 4, lambda r: r, 16, int),
    ("Прибавить 1", 4, lambda r: r + 1, 17, int),
    ("Перевести в строку", 4, lambda r: str(r), "16", str),
    ("Умножить на 3", 4, lambda r: r * 3, 48, int),
    ("Квадрат нуля", 0, lambda r: r, 0, int),
    ("Квадрат отрицательного", -3, lambda r: r, 9, int),
]
for name, x, continuation, expected, result_type in checks_4_1:
    result = square_cps(x, continuation)
    assert result == expected
    assert type(result) is result_type
    print(f"{name}: квадрат {x} = {square(x)} -> {result!r}, тип {type(result).__name__}")

# В square_cps передаётся сама функция k, а не результат её вызова.


# Задание 4.2
# (x + 2) ** 2: два шага через продолжения

def add_cps(a, b, k):
    return k(a + b)


def compute_direct(x):
    return (x + 2) ** 2


def compute_cps(x, k):
    return add_cps(x, 2, lambda s: square_cps(s, k))


print("\nЗадание 4.2")
checks_4_2 = [
    (3, 25),
    (0, 4),
    (-2, 0),
    (-5, 9),
    (4, 36),
]
for x, expected in checks_4_2:
    direct = compute_direct(x)
    result = compute_cps(x, lambda r: r)
    assert direct == result == expected
    print(f"x={x}: обычная={direct}, CPS={result}")

result_plus_10 = compute_cps(3, lambda r: r + 10)
assert result_plus_10 == 35
print(f"x=3, продолжение +10 -> {result_plus_10}")
print("Трассировка при x=3: 3+2=5 -> s=5 -> 5*5=25 -> k(25)=25")
print("С продолжением +10: k(25)=35. Конечное k вызывается после квадрата.")


# Задание 4.3
# Вычисление 2 * (x + 3) в прямом стиле и CPS

def double_cps(x, k):
    return k(2 * x)


def expression_direct(x):
    return 2 * (x + 3)


def expression_cps(x, k):
    return add_cps(x, 3, lambda s: double_cps(s, k))


print("\nЗадание 4.3")
checks_4_3 = [
    (-5, -4),
    (-3, 0),
    (0, 6),
    (2, 10),
    (7, 20),
]
for x, expected in checks_4_3:
    direct = expression_direct(x)
    cps = expression_cps(x, lambda r: r)
    assert direct == cps == expected
    print(f"x={x}: обычная={direct}, CPS={cps}")

assert expression_cps(0, lambda r: r + 5) == 11
print("x=0, продолжение +5 ->", expression_cps(0, lambda r: r + 5))


# Задание 4.4
# Два обработчика: успешное деление и ошибка

def divide_cps(a, b, on_success, on_error):
    if b == 0:
        return on_error("division by zero")
    return on_success(a / b)


print("\nЗадание 4.4")
checks_4_4 = [
    (10, 2, 5.0, "success"),
    (0, 5, 0.0, "success"),
    (-9, 3, -3.0, "success"),
    (1, 3, 1 / 3, "success"),
    (10, 0, "Ошибка: division by zero", "error"),
    (0, 0, "Ошибка: division by zero", "error"),
]
for a, b, expected, expected_handler in checks_4_4:
    calls = []

    def on_success(value):
        calls.append("success")
        return value

    def on_error(message):
        calls.append("error")
        return f"Ошибка: {message}"

    result = divide_cps(a, b, on_success, on_error)
    if expected_handler == "success":
        assert isclose(result, expected, rel_tol=1e-9, abs_tol=1e-9)
    else:
        assert result == expected
    assert calls == [expected_handler]
    print(f"{a} / {b} -> {result}, вызван: {calls[0]}")

# В каждом вызове срабатывает только один из двух обработчиков.


# Задание 4.5 — вариант 17
# E(x) = (x + 20) * (x - 4)

def courier_expression(x):
    return (x + 20) * (x - 4)


def add20_cps(x, k):
    return k(x + 20)


def subtract4_cps(x, k):
    return k(x - 4)


def multiply_cps(a, b, k):
    return k(a * b)


def courier_expression_cps(x, k):
    return add20_cps(
        x,
        lambda first: subtract4_cps(
            x, lambda second: multiply_cps(first, second, k)
        )
    )


print("\nЗадание 4.5 — вариант 17")
checks_4_5 = [
    (-20, 0),
    (-5, -135),
    (0, -80),
    (4, 0),
    (5, 25),
    (10, 180),
]
for x, expected in checks_4_5:
    calls = []

    def keep_number(value):
        calls.append("number")
        return value

    def make_text(value):
        calls.append("text")
        return f"Результат: {value}"

    ordinary = courier_expression(x)
    cps_number = courier_expression_cps(x, keep_number)
    cps_text = courier_expression_cps(x, make_text)
    assert ordinary == cps_number == expected
    assert cps_text == f"Результат: {expected}"
    assert calls == ["number", "text"]
    print(f"x={x}: обычная={ordinary}, k1={cps_number}, k2='{cps_text}'")

print("Трассировка при x=5: 5+20=25 -> 5-4=1 -> 25*1=25 -> k(25)")
print("Каждый этап передаёт результат следующему через продолжение.")


# Задание 4.6 — вариант 17
# R(x, y) = (x - 4) / (y + 20)

def divide_17_cps(a, b, on_success, on_error):
    if b == 0:
        return on_error("zero denominator")
    return on_success(a / b)


def courier_divide_cps(x, y, on_success, on_error):
    return subtract4_cps(
        x,
        lambda numerator: add20_cps(
            y,
            lambda denominator: divide_17_cps(
                numerator, denominator, on_success, on_error
            )
        )
    )


print("\nЗадание 4.6 — вариант 17")
checks_4_6 = [
    (10, -18, 3.0, "success"),
    (4, 0, 0.0, "success"),
    (0, -19, -4.0, "success"),
    (6, -20, "Ошибка: zero denominator", "error"),
    (4, -20, "Ошибка: zero denominator", "error"),
    (0, -21, 4.0, "success"),
    (-2, -17, -2.0, "success"),
]
for x, y, expected, expected_handler in checks_4_6:
    calls = []

    def on_success(value):
        calls.append("success")
        return value

    def on_error(message):
        calls.append("error")
        return f"Ошибка: {message}"

    result = courier_divide_cps(x, y, on_success, on_error)
    if expected_handler == "success":
        assert isclose(result, expected, rel_tol=1e-9, abs_tol=1e-9)
    else:
        assert result == expected
    assert calls == [expected_handler]
    print(f"x={x}, y={y} -> {result}, вызван: {calls[0]}")

# Результат зависит от переданного продолжения.
assert courier_divide_cps(10, -18, lambda r: r, lambda e: e) == 3.0
assert courier_divide_cps(10, -20, lambda r: r, lambda e: e) == "zero denominator"
assert courier_divide_cps(10, -18, lambda r: r * 10, lambda e: e) == 30.0
print("Дополнительное продолжение умножает результат 3.0 на 10 -> 30.0")
print("Трассировка успеха: x=10, y=-18 -> 6/2=3 -> on_success(3)=3")
print("Трассировка ошибки: x=6, y=-20 -> знаменатель 0 -> on_error('zero denominator')")

print("\nВсе проверки блока 4 пройдены.")
