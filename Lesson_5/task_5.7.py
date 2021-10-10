"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json

firms_dic = {}
profit_list = []
with open('task_5.7.txt') as f_obj:
    for line in f_obj.readlines():
        line = line.strip().split()
        firm_res = float(line[2]) - float(line[3])
        firms_dic.update({line[0]: firm_res})
        if firm_res > 0:
            profit_list.append(firm_res)
    res_list = [firms_dic, {'average_profit': int(sum(profit_list) / len(profit_list))}]
with open('task_5.7.json', 'w') as j_obj:
    json.dump(res_list, j_obj)