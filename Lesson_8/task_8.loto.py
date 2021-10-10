"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html"""

import random


class Card:
    def __init__(self):
        self.score = 0
        self.nums = random.sample(range(1, 91), 27)
        self.card_list = [self.nums[:9], self.nums[9:18], self.nums[18:]]
        for line in self.card_list:
            line.sort()
            for idx in random.sample(range(0, 9), 4):
                line[idx] = '  '

    def __str__(self):
        card_view = '\n'.join([' '.join(map(str, line)) for line in self.card_list])
        if self == player_card:
            return '------ Ваша карточка -----\n' + card_view + '\n--------------------------'
        else:
            return '-- Карточка компьютера ---\n' + card_view + '\n--------------------------'

    def check_new_keg(self, keg_num):
        for line in self.card_list:
            if keg_num in line:
                line[line.index(keg_num)] = '-'
                self.score += 1
                return True
            else:
                return False


player_card, comp_card = Card(), Card()
our_kegs = [el for el in range(1, 91)]

while True:
    new_keg = int(input(': '))  # our_kegs.pop(random.randint(0, len(our_kegs) - 1))
    print(f'Новый бочонок: {new_keg}')
    print(f'{player_card}\n{comp_card}')
    print(player_card.score, comp_card.score)
    comp_card.check_new_keg(new_keg)
    player_status = player_card.check_new_keg(new_keg)
    answer = input('Зачеркнуть цифру? (y/n): ').lower()
    if (answer == 'y' and player_status is False) or (answer == 'n' and player_status is True) or comp_card.score == 15:
        print('Вы проиграли!')
        break
    elif player_card.score == 15:
        print('Вы выйграли!')
        break
