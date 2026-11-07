from functools import reduce
from itertools import count, islice
from time import perf_counter
import sys


# Задание 3.1
def safe_divide(a, b):
    if b == 0:
        return 0
    else:
        return a / b


print("Задание 3.1")
print("10 / 2 =", safe_divide(10, 2))
print("10 / 0 =", safe_divide(10, 0))


# Задание 3.2
def take(n, sequence):
    result = []

    for i in range(n):
        result.append(sequence[i])

    return result


sequence = [10, 20, 30, 40, 50, 60, 70]

print("\nЗадание 3.2")
print("Последовательность:", sequence)
print("Первые 5 элементов:", take(5, sequence))


# Задание 3.3
def choose(condition, a, b):
    if condition:
        return a
    else:
        return b


print("\nЗадание 3.3")

try:
    print(choose(True, 1, 1 / 0))
except ZeroDivisionError:
    print("Возникла ошибка деления на ноль")


# Задание 3.4
def natural_numbers():
    number = 1

    while True:
        yield number
        number = number + 1


def first_squares(n):
    numbers = natural_numbers()
    return [x * x for x in islice(numbers, n)]


print("\nЗадание 3.4")
print("Квадраты первых 5 натуральных чисел:", first_squares(5))


# Задание 3.5
def delayed_sum(a, b, condition):
    if condition:
        return a + b
    else:
        return 0


print("\nЗадание 3.5")
print("Условие True:", delayed_sum(5, 10, True))
print("Условие False:", delayed_sum(5, 10, False))

# Задание 3.6
def first_even_generator(n):
    numbers = count(1)
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    return list(islice(even_numbers, n))


def first_even_list(n):
    numbers = list(range(1, n * 2 + 1))
    even_numbers = [x for x in numbers if x % 2 == 0]
    return even_numbers[:n]


n = 100000

print("\nЗадание 3.6")

start = perf_counter()
generator_result = first_even_generator(n)
generator_time = perf_counter() - start

start = perf_counter()
list_result = first_even_list(n)
list_time = perf_counter() - start

list_memory = sys.getsizeof(list(range(1, n * 2 + 1)))
generator_memory = sys.getsizeof(count(1))

print("Количество элементов:", n)
print("Первые 5 значений генератора:", generator_result[:5])
print("Первые 5 значений списка:", list_result[:5])

print("Время генератора:", round(generator_time, 6), "сек.")
print("Время списка:", round(list_time, 6), "сек.")

print("Размер объекта генератора:", generator_memory, "байт")
print("Размер заранее созданного списка:", list_memory, "байт")

# Задание 3.7
def transformation_chain(numbers):
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    squares = list(map(lambda x: x * x, even_numbers))
    result = reduce(lambda a, b: a + b, squares, 0)

    return result, even_numbers, squares


def transformation_loop(numbers):
    result = 0

    for x in numbers:
        if x % 2 == 0:
            result = result + x * x

    return result


numbers_37 = [1, 2, 3, 4, 5, 6]

chain_result, intermediate_even, intermediate_squares = (
    transformation_chain(numbers_37)
)

loop_result = transformation_loop(numbers_37)

print("\nЗадание 3.7")
print("Исходный список:", numbers_37)
print("После filter:", intermediate_even)
print("После map:", intermediate_squares)
print("Результат filter -> map -> reduce:", chain_result)
print("Результат одного цикла:", loop_result)
print("Результаты совпадают:", chain_result == loop_result)

print(
    "Количество элементов в промежуточных списках:",
    len(intermediate_even) + len(intermediate_squares)
)

print("В варианте с одним циклом промежуточные списки не создаются.")
