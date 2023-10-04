import random

import pytest
import math
from pprint import pprint
import random


def test_greeting():
    name = "Анна"
    age = 25

    output = f"Привет, {name}! Тебе {age} лет."
    print(output)
    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    a = 10
    b = 20

    # TODO сосчитайте периметр
    perimeter = (a + b) * 2
    assert perimeter == 60

    # TODO сосчитайте площадь
    area = a * b
    assert area == 200


def test_circle():
    r = 23
    # TODO сосчитайте площадь
    area = math.pi * math.pow(r, 2)
    pprint(area)
    assert area == 1661.9025137490005

    # TODO сосчитайте длину окружности
    length = (2 * math.pi) * r
    pprint(length)
    assert length == 144.51326206513048


def test_random_list():
    # TODO создайте список

    l = sorted([random.randint(1, 100) for i in range(10)])
    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы
    l = set(l)
    l = list(l)
    print(l)
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = dict(zip(first, second))
    print(d.values())
    assert isinstance(d, dict)
    assert len(d) == 5
