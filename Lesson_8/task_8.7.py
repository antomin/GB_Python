"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные
числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата."""


class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}x'

    def __add__(self, other):
        return f'{self.a + other.a} + {self.b + other.b}x'

    def __sub__(self, other):
        return f'{self.a - other.a} + {self.b - other.b}x'

    def __mul__(self, other):
        return f'{((self.a * other.a) - (self.b * other.b)) + ((self.b * other.a) + (self.a * other.b))}x'

    def __truediv__(self, other):
        return f'{((self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2)) + ((self.b * other.a - self.a * other.b) / (other.a ** 2 + other.b ** 2)):.2f}x'


num_1 = ComplexNum(5, 6)
num_2 = ComplexNum(3, 1)
print(num_1)
print(num_2)
print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
print(num_1 / num_2)
