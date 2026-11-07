# Лабораторная работа № 3
# Блок 2. Замыкания и связь окружения с функцией
# Вариант 17 — «Курьерская служба»


# Задание 2.1

def make_shift(offset):
    def shift(value):
        return value + offset
    return shift


shift5 = make_shift(5)
shift10 = make_shift(10)
shift_minus2 = make_shift(-2)
shift20 = make_shift(20)

print("Задание 2.1")
checks_2_1 = [
    (shift5, 3, 8),
    (shift10, 3, 13),
    (shift_minus2, 3, 1),
    (shift20, 3, 23),
    (shift5, 3, 8),
    (shift_minus2, 0, -2),
]

for func, value, expected in checks_2_1:
    result = func(value)
    assert result == expected
    print(f"Смещение: {result - value}, число: {value} -> {result}")

# У shift параметр value, а свободная переменная — offset.
# Каждый вызов make_shift создаёт функцию со своим смещением.


# Задание 2.2

def make_total(start):
    total = start

    def update(delta):
        nonlocal total
        total += delta
        return total

    return update


first = make_total(10)
second = make_total(100)

print("\nЗадание 2.2")
checks_2_2 = [
    ("Первый", first, 3, 13),
    ("Второй", second, 1, 101),
    ("Первый", first, 2, 15),
    ("Второй", second, -10, 91),
    ("Первый", first, -5, 10),
    ("Второй", second, 0, 91),
]

for name, func, delta, expected in checks_2_2:
    result = func(delta)
    assert result == expected
    print(f"{name}: изменение {delta} -> {result}")

# nonlocal позволяет изменять total из внешней функции.
# У двух накопителей состояния независимы.


# Задание 2.3

def make_interval(low, high):
    if low > high:
        raise ValueError("Нижняя граница больше верхней")

    def contains(value):
        return low <= value <= high

    return contains


interval1 = make_interval(-5, 5)
interval2 = make_interval(10, 20)

print("\nЗадание 2.3")
checks_2_3 = [
    ("[-5, 5]", interval1, -5, True),
    ("[-5, 5]", interval1, 5, True),
    ("[-5, 5]", interval1, -6, False),
    ("[-5, 5]", interval1, 6, False),
    ("[10, 20]", interval2, 10, True),
    ("[10, 20]", interval2, 20, True),
    ("[10, 20]", interval2, 9, False),
    ("[10, 20]", interval2, 21, False),
]

for name, func, value, expected in checks_2_3:
    result = func(value)
    assert result == expected
    print(f"Интервал {name}, число {value} -> {result}")

try:
    make_interval(8, 2)
    assert False, "Ожидалась ошибка ValueError"
except ValueError:
    print("Неверные границы (8, 2) -> ValueError")


# Задание 2.4

def make_sequence(start, step):
    next_value = start

    def get_next():
        nonlocal next_value
        result = next_value
        next_value += step
        return result

    return get_next


sequence1 = make_sequence(1, 2)
sequence2 = make_sequence(10, -3)

print("\nЗадание 2.4")
checks_2_4 = [
    ("Первая", sequence1, 1),
    ("Вторая", sequence2, 10),
    ("Первая", sequence1, 3),
    ("Вторая", sequence2, 7),
    ("Первая", sequence1, 5),
    ("Вторая", sequence2, 4),
    ("Первая", sequence1, 7),
    ("Вторая", sequence2, 1),
]

for name, func, expected in checks_2_4:
    result = func()
    assert result == expected
    print(f"{name} последовательность -> {result}")


# Задание 2.5 (вариант 17)

def make_transform(a, b):
    def transform(x):
        return a * x + b

    return transform


transform1 = make_transform(4, 20)
transform2 = make_transform(5, 22)

print("\nЗадание 2.5 — вариант 17")
checks_2_5 = [
    ("4*x + 20", transform1, 0, 20),
    ("5*x + 22", transform2, 0, 22),
    ("4*x + 20", transform1, 3, 32),
    ("5*x + 22", transform2, 3, 37),
    ("4*x + 20", transform1, -2, 12),
    ("5*x + 22", transform2, -2, 12),
    ("4*x + 20", transform1, 3, 32),
    ("5*x + 22", transform2, 3, 37),
]

for name, func, value, expected in checks_2_5:
    result = func(value)
    assert result == expected
    print(f"{name}, x = {value} -> {result}")

# Коэффициенты хранятся внутри каждой функции и не меняются.


# Задание 2.6 (вариант 17)

def make_limited_total(start, limit):
    if type(start) is not int or type(limit) is not int or not 0 <= start <= limit:
        raise ValueError("Неверное начальное значение или предел")

    total = start

    def update(delta):
        nonlocal total
        if type(delta) is not int:
            return None

        new_total = total + delta
        if new_total < 0 or new_total > limit:
            return None

        total = new_total
        return total

    return update


courier1 = make_limited_total(22, 71)
courier2 = make_limited_total(10, 30)

print("\nЗадание 2.6 — вариант 17")
checks_2_6 = [
    ("Первый", courier1, 8, 30),
    ("Второй", courier2, 5, 15),
    ("Первый", courier1, 40, 70),
    ("Второй", courier2, -5, 10),
    ("Первый", courier1, 2, None),    # Больше 71
    ("Первый", courier1, 0, 70),      # После ошибки сумма не изменилась
    ("Второй", courier2, -11, None), # Меньше 0
    ("Второй", courier2, 0, 10),     # После ошибки сумма не изменилась
    ("Первый", courier1, "2", None), # Неверный тип delta
    ("Первый", courier1, 0, 70),      # После ошибки сумма не изменилась
    ("Первый", courier1, -20, 50),   # Отрицательный delta допустим
    ("Второй", courier2, 15, 25),
    ("Первый", courier1, -51, None),
    ("Первый", courier1, 0, 50),
]

for name, func, delta, expected in checks_2_6:
    result = func(delta)
    assert result == expected
    print(f"{name}: изменение {delta!r} -> {result}")

invalid_settings = [(-1, 71), (72, 71), (10, 5), (10.0, 71)]
for start, limit in invalid_settings:
    try:
        make_limited_total(start, limit)
        assert False, "Ожидалась ошибка ValueError"
    except ValueError:
        print(f"Начало {start}, предел {limit} -> ValueError")


print("\nВсе проверки блока 2 пройдены.")
