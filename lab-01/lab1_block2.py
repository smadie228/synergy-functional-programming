# Задание 2.1
def sum_to_n(n):
    result = 0

    for i in range(1, n + 1):
        result = result + i

    return result


print("Задание 2.1")
print("Сумма чисел от 1 до 5:", sum_to_n(5))


# Задание 2.2
def count_even_loop(numbers):
    count = 0

    for x in numbers:
        if x % 2 == 0:
            count = count + 1

    return count


numbers = [1, 2, 3, 4, 5, 6]

print("\nЗадание 2.2")
print("Список:", numbers)
print("Количество чётных чисел:", count_even_loop(numbers))


# Задание 2.3
def count_even_filter(numbers):
    return len(list(filter(lambda x: x % 2 == 0, numbers)))


print("\nЗадание 2.3")
print("Количество чётных через filter:", count_even_filter(numbers))
print("Результаты совпадают:",
      count_even_loop(numbers) == count_even_filter(numbers))



# Задание 2.4
from functools import reduce


def max_loop(numbers):
    maximum = numbers[0]

    for x in numbers:
        if x > maximum:
            maximum = x

    return maximum


def max_reduce(numbers):
    return reduce(lambda a, b: a if a > b else b, numbers)


numbers_max = [3, 7, 1, 9, 4]

print("\nЗадание 2.4")
print("Список:", numbers_max)
print("Максимум через цикл:", max_loop(numbers_max))
print("Максимум через reduce:", max_reduce(numbers_max))
print("Результаты совпадают:",
      max_loop(numbers_max) == max_reduce(numbers_max))


# Задание 2.5
def squares_loop(numbers):
    result = []

    for x in numbers:
        result.append(x * x)

    return result


def squares_map(numbers):
    return list(map(lambda x: x * x, numbers))


numbers_square = [1, 2, 3, 4]

print("\nЗадание 2.5")
print("Список:", numbers_square)
print("Квадраты через цикл:", squares_loop(numbers_square))
print("Квадраты через map:", squares_map(numbers_square))
print("Результаты совпадают:",
      squares_loop(numbers_square) == squares_map(numbers_square))



# Задание 2.6
def sum_even_squares_loop(numbers):
    result = 0

    for x in numbers:
        if x % 2 == 0:
            result = result + x * x

    return result


def sum_even_squares_functional(numbers):
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    squares = map(lambda x: x * x, even_numbers)
    return reduce(lambda a, b: a + b, squares, 0)


numbers_26 = [1, 2, 3, 4, 5, 6]

print("\nЗадание 2.6")
print("Список:", numbers_26)
print("Императивный вариант:", sum_even_squares_loop(numbers_26))
print("Декларативный вариант:", sum_even_squares_functional(numbers_26))
print(
    "Результаты совпадают:",
    sum_even_squares_loop(numbers_26)
    == sum_even_squares_functional(numbers_26)
)


# Задание 2.7
def add_without_change(numbers, x):
    return numbers + [x]


def add_with_change(numbers, x):
    numbers.append(x)
    return numbers


original_list_1 = [1, 2, 3]
new_list = add_without_change(original_list_1, 4)

print("\nЗадание 2.7")
print("Без изменения исходного списка:")
print("Исходный список:", original_list_1)
print("Новый список:", new_list)

original_list_2 = [1, 2, 3]
changed_list = add_with_change(original_list_2, 4)

print("\nС изменением исходного списка:")
print("Исходный список после вызова:", original_list_2)
print("Результат функции:", changed_list)