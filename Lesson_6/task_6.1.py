"""
Создать класс (светофор).

- определить у него один атрибут color (цвет) и метод running (запуск);
- атрибут реализовать как приватный;
- в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
- продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) на
ваше усмотрение;
- переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
- проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
завершать скрипт."""

from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = ['красный', 'жёлтый', 'зелёный']

    def running(self):
        while True:
            print(self.__color[0])
            sleep(7)
            print(self.__color[1])
            sleep(2)
            print(self.__color[2])
            sleep(5)


tr = TrafficLight()
tr.running()