"""
Реализуйте базовый класс Car.

- у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
- опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
- добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
- для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
методы и покажите результат."""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} поехал.')

    def stop(self):
        print(f'{self.color} {self.name} остановился.')

    def turn(self, direction):
        print(f'{self.color} {self.name} повернул {direction}')

    def show_speed(self):
        print(f'Скорость - {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Скорость превышена!!!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Скорость превышена!!!')


class PoliceCar(Car):
    pass


t_car = TownCar(65, 'Желтая', 'москвич', False)
t_car.go()
t_car.show_speed()

s_car = SportCar(165, 'Красный', 'Lamborghini', False)
s_car.stop()
s_car.show_speed()

w_car = WorkCar(50, 'Зелёный', 'Трактор', False)
w_car.turn('налево')
w_car.show_speed()

p_car = PoliceCar(45, 'Синий', 'бобик', True)
p_car.turn('направо')
p_car.show_speed()
