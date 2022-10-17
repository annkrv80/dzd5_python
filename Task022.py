import os
from random import randint, random
def clear(): return os.system('cls')


clear()
con = 2021
count = 0
step_max=28
player1 = input('Я Маруся! Давай поиграем? Kak твое имя? ')
player2 = 'Бот-Маруся'
print('Определим правило первого хода')
a = randint(0, 1)
print(a)
if a == 0:
    count = 0
    print(f'{player1} делай первый ход!')

else:
    count = 1
    print(f'{player2} делает первый ход!')

print(f'На столе лежит {con} конфета')
while con > 0:
    if count == 0:
        step = int(input(f'{player1} бери конфеты '))
        if step > con:
            print('Столько конфет нет.Попробуй снова!')
        elif step > step_max:
            print(f'Максимальный ход {step_max} конфет!')
        else:
            con = con-step
            if con > 0:
                print(f'На кону {con}')
                count = 1

    if count == 1:
        if con > 41:
           step = randint(1, step_max)
        if 30 < con < 40:
            step = con-(step_max+1)
        if con < (step_max+1):
            step = con

        print(f'Маруся берет {step}')
        con = con-step
        if con > 0:

            print(f'На кону {con}')
            count = 0

if count == 0:
    print(f'{player1} ПОБЕДА!!!')
else:
    print(f'{player2} ПОБЕДА!!!')
