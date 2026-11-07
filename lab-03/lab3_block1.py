# Лабораторная работа № 3
# Блок 1. Сопоставление с образцом
# Вариант 17 — «Курьерская служба»


# Задание 1.1

def describe(message):
    match message:
        case ("value", int(n)) if n >= 0:
            return f"Значение: {n}"
        case ("empty",):
            return "Нет данных"
        case ("error", str(text)):
            return f"Ошибка: {text}"
        case _:
            return "Неверное сообщение"


print("\nЗадание 1.1")

checks_1_1 = [
    (("value", 7), "Значение: 7"),
    (("empty",), "Нет данных"),
    (("value", -1), "Неверное сообщение"),
    (("error", "сбой"), "Ошибка: сбой"),
    (("unknown", 5), "Неверное сообщение"),
]

for message, expected in checks_1_1:
    result = describe(message)
    assert result == expected
    print(message, "->", result)


# Задание 1.2

def access(record):
    match record:
        case {"state": "active", "score": int(s)} if s >= 50:
            return "Допуск"
        case {"state": "active", "score": int(s)} if s >= 0:
            return "Недостаточно баллов"
        case {"state": "blocked"}:
            return "Доступ закрыт"
        case _:
            return "Неверные данные"


print("\nЗадание 1.2")

checks_1_2 = [
    ({"state": "active", "score": 70}, "Допуск"),
    ({"state": "active", "score": 10}, "Недостаточно баллов"),
    ({"state": "active", "score": -1}, "Неверные данные"),
    ({"state": "blocked"}, "Доступ закрыт"),
    ({"state": "blocked", "score": 100}, "Доступ закрыт"),
    ({"state": "active", "score": 70, "note": "ok"}, "Допуск"),
    ({}, "Неверные данные"),
]

for record, expected in checks_1_2:
    result = access(record)
    assert result == expected
    print(record, "->", result)


# Задание 1.3

def describe_list(values):
    match values:
        case []:
            return "empty"
        case [item]:
            return ("one", item)
        case [first, *rest]:
            return ("many", first, len(rest))


print("\nЗадание 1.3")

checks_1_3 = [
    ([], "empty"),
    ([10], ("one", 10)),
    ([10, 20], ("many", 10, 1)),
    ([1, 2, 3, 4, 5], ("many", 1, 4)),
]

for values, expected in checks_1_3:
    result = describe_list(values)
    assert result == expected
    print(values, "->", result)


# Задание 1.4

def classify_reading(record):
    match record:
        case {"kind": "temperature", "value": int(x)} if -50 <= x <= 50:
            return "normal"
        case {"kind": "temperature", "value": int(x)}:
            return "alarm"
        case {"kind": "offline"}:
            return "offline"
        case _:
            return "invalid"


print("\nЗадание 1.4")

checks_1_4 = [
    ({"kind": "temperature", "value": 0}, "normal"),
    ({"kind": "temperature", "value": -50}, "normal"),
    ({"kind": "temperature", "value": 50}, "normal"),
    ({"kind": "temperature", "value": -51}, "alarm"),
    ({"kind": "temperature", "value": 51}, "alarm"),
    ({"kind": "offline"}, "offline"),
    ({"kind": "temperature", "value": 20, "unit": "C"}, "normal"),
    ({"kind": "temperature", "value": "20"}, "invalid"),
    ({}, "invalid"),
]

for record, expected in checks_1_4:
    result = classify_reading(record)
    assert result == expected
    print(record, "->", result)


# Задание 1.5 (вариант 17)

def parcel_message(message):
    match message:
        case ("parcel", int(x)) if x >= 0:
            return x + 20
        case ("distance", int(x)) if x >= 0:
            return 4 * x
        case ("stop",):
            return 17
        case _:
            return None


print("\nЗадание 1.5 — вариант 17")

checks_1_5 = [
    (("parcel", 5), 25),
    (["parcel", 0], 20),
    (("distance", 3), 12),
    (["distance", 0], 0),
    (("stop",), 17),
    (("parcel", -2), None),
    (("distance", "4"), None),
    (("parcel", 1, 2), None),
    (("other", 5), None),
]

for message, expected in checks_1_5:
    result = parcel_message(message)
    assert result == expected
    print(message, "->", result)


# Задание 1.6 (вариант 17)

def classify_parcel(record):
    match record:
        case {"status": "active", "value": int(x)} if 0 <= x < 44:
            return "low"
        case {"status": "active", "value": int(x)} if x >= 44:
            return "high"
        case {"status": "paused"}:
            return "paused"
        case _:
            return "invalid"


print("\nЗадание 1.6 — вариант 17")

checks_1_6 = [
    ({"status": "active", "value": 0}, "low"),
    ({"status": "active", "value": 43}, "low"),
    ({"status": "active", "value": 44}, "high"),
    ({"status": "active", "value": 70}, "high"),
    ({"status": "paused"}, "paused"),
    ({"status": "paused", "value": "любое"}, "paused"),
    ({"status": "active", "value": 50, "extra": True}, "high"),
    ({"status": "active", "value": -1}, "invalid"),
    ({"status": "active", "value": "50"}, "invalid"),
    ({"status": "active"}, "invalid"),
    ({"status": "unknown", "value": 10}, "invalid"),
    ({}, "invalid"),
]

for record, expected in checks_1_6:
    result = classify_parcel(record)
    assert result == expected
    print(record, "->", result)

print("\nВсе проверки блока 1 пройдены.")
