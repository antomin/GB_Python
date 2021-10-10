"""
Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных
о пользователе одной строкой.
"""


def my_func(name, surname, year_of_birth, hometown, email, phone):
    print(f'Имя: {name}, фамилия: {surname}, год рождения: {year_of_birth}, город проживания: {hometown}, email: {email}, телефон: {phone}.')


my_func(name='Ivan', surname='Ivanov', year_of_birth='01.01.1990', hometown='Ivanovo', email='ivan@ivanov.ru', phone='+79001112233')
