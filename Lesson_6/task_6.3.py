"""
Реализовать базовый класс Worker (работник).

- определить атрибуты: name, surname, position (должность), income (доход);
- последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus};
- создать класс Position (должность) на базе класса Worker;
- в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
(get_total_income);
- проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров."""


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


pers_1 = Position('Ivan', 'Ivanov', 'Manager', {"wage": 50000, "bonus": 17000})
pers_2 = Position('Sidr', 'Sidorovich', 'Worker', {"wage": 20000, "bonus": 3000})
print(pers_1.get_full_name())
print(pers_1.get_total_income())
print(pers_2.get_full_name())
print(pers_2.get_total_income())
