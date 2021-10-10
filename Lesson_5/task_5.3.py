"""
Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10
строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт
средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

low_salary_list = []
all_res = 0
with open('task_5.3.txt') as f_obj:
    for line in f_obj.readlines():
        if float(line.split()[1]) < 20000.00:
            low_salary_list.append(line.split()[0])
        all_res += float(line.split()[1])
    print(f"{', '.join(low_salary_list)} получают менее 20000")
    f_obj.seek(0)
    print(f'Средняя ЗП: {all_res / len(f_obj.readlines())}')
