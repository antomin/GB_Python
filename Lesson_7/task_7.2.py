"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod


class MyAbstract(ABC):
    @abstractmethod
    def coat(self):
        pass

    @abstractmethod
    def costume(self):
        pass

    @abstractmethod
    def all_consumption(self):
        pass


class Clothes(MyAbstract):
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def coat(self):
        self.coat_consumption = round(self.v / 6.5 + 0.5, 2)
        return f'На пальто - {self.coat_consumption} м ткани'

    @property
    def costume(self):
        self.costume_consumption = round(2 * self.h + 0.3, 2)
        return f'На костюм - {self.coat_consumption} м ткани'

    @property
    def all_consumption(self):
        return f'На всё - {self.coat_consumption + self.costume_consumption} м ткани'


my_size = Clothes(46, 1.8)
print(my_size.coat)
print(my_size.costume)
print(my_size.all_consumption)
