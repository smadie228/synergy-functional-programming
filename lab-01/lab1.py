# Задание 1.1
def cube(x):
    return x * x * x

print("Задание 1.1")
print("cube(2) =", cube(2))
print("cube(3) =", cube(3))
print("cube(4) =", cube(4))

# Задание 1.2
def sum_three(a, b, c):
    return a + b + c

print("\nЗадание 1.2")
print("sum_three(1, 2, 3) =", sum_three(1, 2, 3))
print("sum_three(5, 10, 15) =", sum_three(5, 10, 15))
print("sum_three(-2, 4, 8) =", sum_three(-2, 4, 8))

# Задание 1.3
counter = 0

def next_number():
    global counter
    counter = counter + 1
    return counter

print("\nЗадание 1.3")
print("Первый вызов:", next_number())
print("Второй вызов:", next_number())
print("Третий вызов:", next_number())

# Задание 1.4
def increase(value):
    return value + 1

print("\nЗадание 1.4")
print("increase(5) =", increase(5))
print("increase(5) =", increase(5))
print("increase(10) =", increase(10))

# Задание 1.5
def process_list(numbers):
    positive_numbers = filter(lambda x: x > 0, numbers)
    return list(map(lambda x: x * 2, positive_numbers))

numbers = [-1, 2, -3, 4, 5]

print("\nЗадание 1.5")
print("Исходный список:", numbers)
print("Результат:", process_list(numbers))

# Задание 1.6
def normalize(numbers):
    maximum = max(numbers)

    if maximum == 0:
        return numbers.copy()

    return list(map(lambda x: x / maximum, numbers))


numbers_normalize = [2, 4, 6, 8]

print("\nЗадание 1.6")
print("Исходный список:", numbers_normalize)
print("Результат:", normalize(numbers_normalize))
print("Исходный список после вызова:", numbers_normalize)

# Задание 1.7
from functools import reduce

def impure_sum(numbers):
    result = 0

    for x in numbers:
        result = result + x

    return result


def pure_sum(numbers):
    return reduce(lambda a, b: a + b, numbers, 0)


numbers_sum = [1, 2, 3, 4, 5]

print("\nЗадание 1.7")
print("Список:", numbers_sum)
print("Сумма с циклом:", impure_sum(numbers_sum))
print("Сумма через reduce:", pure_sum(numbers_sum))