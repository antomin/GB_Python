"""
Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных,
практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно, чтобы для
каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
Примеры строк файла:
Информатика:   100(л)   50(пр)   20(лаб).
Физика:   30(л)   —   10(лаб)
Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

res_dic = {}
with open('task_5.6.txt') as f_obj:
    while True:
        line = f_obj.readline()
        if not line:
            break
        hours_res = [el.split('(')[0] for el in line.split() if el[0].isdigit()]
        res_dic.update({line.split(':')[0]: sum(list(map(int, hours_res)))})
print(res_dic)
