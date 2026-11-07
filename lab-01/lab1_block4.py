# Задание 4.1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print("Задание 4.1")
print("Факториал 5:", factorial(5))


# Задание 4.2
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


print("\nЗадание 4.2")
print("2 в степени 10:", power(2, 10))


# Задание 4.3
def tail_sum(n, accumulator):
    if n == 0:
        return accumulator
    else:
        return tail_sum(n - 1, accumulator + n)


print("\nЗадание 4.3")
print("Сумма от 1 до 5:", tail_sum(5, 0))


# Задание 4.4
def normal_sum(n):
    if n == 0:
        return 0
    else:
        return n + normal_sum(n - 1)


def tail_sum_44(n, accumulator=0):
    if n == 0:
        return accumulator
    else:
        return tail_sum_44(n - 1, accumulator + n)


print("\nЗадание 4.4")
print("Обычная рекурсия:", normal_sum(5))
print("Хвостовая рекурсия:", tail_sum_44(5))


# Задание 4.5
def factorial_normal(n):
    if n == 0:
        return 1
    else:
        return n * factorial_normal(n - 1)


def factorial_tail(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return factorial_tail(n - 1, accumulator * n)


print("\nЗадание 4.5")
print("Обычный факториал:", factorial_normal(5))
print("Хвостовой факториал:", factorial_tail(5))


# Задание 4.6
def reverse_list(numbers, accumulator=None):
    if accumulator is None:
        accumulator = []

    if len(numbers) == 0:
        return accumulator

    return reverse_list(numbers[1:], [numbers[0]] + accumulator)


numbers_46 = [1, 2, 3, 4, 5]

print("\nЗадание 4.6")
print("Исходный список:", numbers_46)
print("Обратный список:", reverse_list(numbers_46))


# Задание 4.7
def count_element(numbers, element, accumulator=0):
    if len(numbers) == 0:
        return accumulator

    if numbers[0] == element:
        accumulator = accumulator + 1

    return count_element(numbers[1:], element, accumulator)


numbers_47 = [1, 2, 2, 3, 2, 4]

print("\nЗадание 4.7")
print("Список:", numbers_47)
print("Искомый элемент: 2")
print("Количество:", count_element(numbers_47, 2))


# Задание 4.8
def sum_list_loop(numbers):
    result = 0

    for x in numbers:
        result = result + x

    return result


def sum_list_tail(numbers, accumulator=0):
    if len(numbers) == 0:
        return accumulator

    return sum_list_tail(numbers[1:], accumulator + numbers[0])


numbers_48 = [1, 2, 3, 4, 5]

print("\nЗадание 4.8")
print("Список:", numbers_48)
print("Сумма через цикл:", sum_list_loop(numbers_48))
print("Сумма через хвостовую рекурсию:", sum_list_tail(numbers_48))
print(
    "Результаты совпадают:",
    sum_list_loop(numbers_48) == sum_list_tail(numbers_48)
)

