"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны
заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

my_dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

# print(my_dic['One'])
with open('task_5.4.txt', 'r') as f_obj:
    for line in f_obj.readlines():
        with open('task_5.4_new.txt', 'a') as f_new_obj:
            f_new_obj.write(line.replace(line.split()[0], my_dic[line.split()[0]]))
