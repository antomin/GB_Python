"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на
экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода пользователем
очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При
этом работа скрипта не должна завершаться."""


class InputError(Exception):
    def __init__(self):
        pass


my_lst = []
while True:
    new_el = input('Введите число или "stop" для выхдода: ')
    if new_el == 'stop':
        print(my_lst)
        break
    try:
        if not new_el.isdigit():
            raise InputError()
    except InputError:
        print(f'{new_el} - не число!')
        continue
    my_lst.append(int(new_el))

