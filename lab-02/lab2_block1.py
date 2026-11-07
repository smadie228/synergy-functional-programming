
# Задание 1.1

def my_map(f, xs):
    result = []
    for x in xs:
        result.append(f(x))
    return result


def my_filter(pred, xs):
    result = []
    for x in xs:
        if pred(x):
            result.append(x)
    return result


def my_fold_left(f, init, xs):
    result = init
    for x in xs:
        result = f(result, x)
    return result


def my_zip_with(f, xs, ys):
    result = []
    i = 0
    while i < len(xs) and i < len(ys):
        result.append(f(xs[i], ys[i]))
        i += 1
    return result


numbers = [1, 2, 3, 4, 5]

print("Проверка my_map:",
      my_map(lambda x: x * 2, numbers))

print("Проверка my_filter:",
      my_filter(lambda x: x % 2 == 0, numbers))

print("Проверка my_fold_left:",
      my_fold_left(lambda a, b: a + b, 0, numbers))

print("Проверка my_zip_with:",
      my_zip_with(lambda a, b: a + b,
                  [1, 2, 3], [10, 20, 30]))


print("Длина списка:",
      my_fold_left(lambda a, x: a + 1, 0, numbers))

print("Сумма:",
      my_fold_left(lambda a, x: a + x, 0, numbers))

print("Произведение:",
      my_fold_left(lambda a, x: a * x, 1, numbers))

print("Максимум:",
      my_fold_left(lambda a, x: x if x > a else a,
                   numbers[0], numbers[1:]))

print("Реверс:",
      my_fold_left(lambda a, x: [x] + a, [], numbers))


# Задание 1.2

def curry2(f):
    def first(x):
        def second(y):
            return f(x, y)
        return second
    return first


def uncurry2(f):
    def result(x, y):
        return f(x)(y)
    return result


def multiply(a, b):
    return a * b


curried = curry2(multiply)
print("\nЗадание 1.2")
print("curry2:", curried(3)(4))

uncurried = uncurry2(curried)
print("uncurry2:", uncurried(3, 4))


def add(x):
    return lambda y: x + y


add5 = add(5)
add10 = add(10)

print("add5:", add5(3))
print("add10:", add10(3))


def compose(f, g):
    return lambda x: f(g(x))


def pipe(f, g):
    return lambda x: g(f(x))


def double(x):
    return x * 2


def inc(x):
    return x + 1


def square(x):
    return x * x


print("compose:", compose(double, inc)(5))
print("pipe:", pipe(double, inc)(5))


left = compose(double, compose(inc, square))
right = compose(compose(double, inc), square)

for x in [1, 2, 5]:
    print("Ассоциативность при x =", x)
    print("Левая часть:", left(x))
    print("Правая часть:", right(x))
    print("Результаты равны:", left(x) == right(x))


# Задание 1.3

def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter1 = make_counter()
counter2 = make_counter()

print("\nЗадание 1.3")
print("Первый счётчик:", counter1())
print("Первый счётчик:", counter1())
print("Первый счётчик:", counter1())
print("Второй счётчик:", counter2())


def power(n):
    def result(x):
        return x ** n
    return result


square = power(2)
cube = power(3)

print("Квадрат числа 4:", square(4))
print("Куб числа 4:", cube(4))



# Задание 1.4

from itertools import groupby
from functools import reduce

products = [
    {"name": "Мышь", "category": "Электроника", "price": 900},
    {"name": "Клавиатура", "category": "Электроника", "price": 1600},
    {"name": "Наушники", "category": "Электроника", "price": 2500},
    {"name": "Блокнот", "category": "Канцелярия", "price": 250},
    {"name": "Ручка", "category": "Канцелярия", "price": 80},
    {"name": "Папка", "category": "Канцелярия", "price": 170}
]

print("\nЗадание 1.4")

# Товары дороже 1000 рублей
n = 1000
expensive = list(filter(lambda x: x["price"] > n, products))
print("Товары дороже 1000:", expensive)

# Сортировка по цене
by_price = sorted(products, key=lambda x: x["price"])
print("Сортировка по цене:", by_price)

# Сортировка по названию
by_name = sorted(products, key=lambda x: x["name"])
print("Сортировка по названию:", by_name)

# Группировка по категориям
by_category = sorted(products, key=lambda x: x["category"])

groups = dict(map(
    lambda item: (item[0], list(item[1])),
    groupby(by_category, key=lambda x: x["category"])
))

print("Группы товаров:", groups)

# Самый дорогой товар в каждой категории
max_products = dict(map(
    lambda item: (
        item[0],
        max(item[1], key=lambda x: x["price"])
    ),
    groups.items()
))

print("Самые дорогие товары:", max_products)

# Суммарная стоимость
total = reduce(
    lambda result, x: result + x["price"],
    products,
    0
)

print("Общая стоимость:", total)
