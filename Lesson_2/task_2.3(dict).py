"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна,
лето, осень). Напишите решения через list и через dict.
"""

month = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Авгусст', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}

while True:
    try:
        num_month = int(input('Введите номер месяца от 1 до 12: '))
        if num_month > 12 or num_month < 1:
            print('Неверные данные!')
            continue
        else:
            if num_month == 12 or num_month == 1 or num_month == 2:
                print(f'{month.get(num_month)} - Зима')
            elif num_month == 3 or num_month == 4 or num_month == 5:
                print(f'{month.get(num_month)} - Весна')
            elif num_month == 6 or num_month == 7 or num_month == 8:
                print(f'{month.get(num_month)} - Лето')
            else:
                print(f'{month.get(num_month)} - Осень')
        break
    except ValueError:
        print('Неверные данные!')
