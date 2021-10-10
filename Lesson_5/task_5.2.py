"""
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
"""

with open('task_5.2.txt') as f_obj:
    my_txt = f_obj.readlines()
    print(f'В тексте {len(my_txt)} строки')
    for idx, line in enumerate(my_txt, 1):
        print(f'В строке {idx} слов: {len(line.split())}')
