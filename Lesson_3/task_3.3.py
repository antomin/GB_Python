"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух
аргументов.
"""


def my_func(a, b, c):
    return a + b + c - min(a, b, c)


print(my_func(10, 11, 12))
