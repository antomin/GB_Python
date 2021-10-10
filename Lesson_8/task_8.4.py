"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для
каждого типа оргтехники."""


class Storage:
    def __init__(self, address, square):
        self.address = address
        self.square = square


class Equipment:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Computer(Equipment):
    def __init__(self, brand, model, hdd_size, ram_size, os):
        super().__init__(brand, model)
        self.hdd_size = hdd_size
        self.ram_size = ram_size
        self.os = os


class Printer(Equipment):
    def __init__(self, brand, model, print_speed, is_multi):
        super().__init__(brand, model)
        self.print_speed = print_speed
        self.is_multi = is_multi


class Monitor(Equipment):
    def __init__(self, brand, model, matrix, size):
        super().__init__(brand, model)
        self.matrix = matrix
        self.size = size
