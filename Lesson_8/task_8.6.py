"""
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП."""


class Storage:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.left_equip = {}

    def accept_equip(self, equip, num):
        try:
            int(num)
            if str(equip) in self.left_equip.keys():
                self.left_equip[str(equip)] += num
            else:
                self.left_equip[str(equip)] = num
            print(f'{equip} в кол-ве {num} шт. принято на склад {self.name}')
        except ValueError:
            print('Введите правильное кол-во')

    def send_equip(self, equip, num, target):
        try:
            int(num)
            if str(equip) not in self.left_equip.keys() or num > self.left_equip[str(equip)]:
                print('Не хватает количества.')
            else:
                self.left_equip[str(equip)] -= num
                print(f'{equip} в кол-ве {num} шт. отправленно в {target}')
        except ValueError:
            print('Введите правильное кол-во!')


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

    def __str__(self):
        return f'Компьютер ({self.brand}-{self.model}/{self.hdd_size}/{self.ram_size}/{self.os})'


class Printer(Equipment):
    def __init__(self, brand, model, print_speed, is_multi):
        super().__init__(brand, model)
        self.print_speed = print_speed
        self.is_multi = is_multi

    def __str__(self):
        if self.is_multi:
            return f'Принтер ({self.brand}-{self.model}/{self.print_speed}стр/Мультифункциональный)'
        else:
            return f'Принтер ({self.brand}-{self.model}/{self.print_speed}стр)'


class Monitor(Equipment):
    def __init__(self, brand, model, matrix, size):
        super().__init__(brand, model)
        self.matrix = matrix
        self.size = size

    def __str__(self):
        return f'Монитор ({self.brand}-{self.model}/{self.matrix}/{self.size})'


store_1 = Storage('Главный', 'Пушкина 1-2')
comp_1 = Computer('HP', 'as32', 250, 8, 'Linux')
comp_2 = Computer('Asus', 'a2', 500, 4, 'Windows')
print_1 = Printer('Samsung', 'qwe1', 100, True)
print_2 = Printer('HP', '12er', 50, False)
mon_1 = Monitor('Sony', '1234a', 'IPS', 19)
mon_2 = Monitor('Xiaomi', '1AAA', 'TFT', 21)

store_1.accept_equip(comp_2, 2)
store_1.send_equip(comp_2, 2, 'qwe')