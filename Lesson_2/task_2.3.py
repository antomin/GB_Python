"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна,
лето, осень). Напишите решения через list и через dict.
"""

month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Авгусст', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

while True:
    try:
        num_month = int(input('Введите номер месяца от 1 до 12: '))
        if num_month > 12 or num_month < 1:
            print('Неверные данные!')
            continue
        else:
            if num_month == 12 or num_month == 1 or num_month == 2:
                print(f'{month[num_month - 1]} - Зима')
            elif num_month == 3 or num_month == 4 or num_month == 5:
                print(f'{month[num_month - 1]} - Весна')
            elif num_month == 6 or num_month == 7 or num_month == 8:
                print(f'{month[num_month - 1]} - Лето')
            else:
                print(f'{month[num_month - 1]} - Осень')
        break
    except ValueError:
        print('Неверные данные!')
