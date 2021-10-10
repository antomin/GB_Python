"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class Date:
    def __init__(self, date_str):
        self.data_str = date_str

    @classmethod
    def extract_date(cls, date_str):
        date_lst = list(map(int, date_str.split('-')))
        return cls.validate_date(date_lst[0], date_lst[1], date_lst[2])

    @staticmethod
    def validate_date(day, month, year):
        if day > 30 or day < 1 or month > 12 or month < 1 or year > 2021 or year < 1900:
            return 'Неверная дата'
        else:
            return f'{day}-й день {month}-ого месяца {year}-ого года'


print(Date.extract_date(input('Введите дату ДД-ММ-ГГГГ: ')))
