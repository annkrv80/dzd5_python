#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
#Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
#Все конфеты оппонента достаются сделавшему последний ход.
#Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
import os
from random import randint, random
from turtle import goto
clear=lambda:os.system('cls')
clear()


con = 2021
count = 0
step_max = 28
player1 = input('Введите имя первого игрока ')
player2 = input('Введите имя второго игрока ')
print('Определим правило первого хода')
a = randint(1, 2)
if a == 1:
    one = player1
    two = player2
else:
    one = player2
    two = player1
print(f'Поздравляю {one} ты ходишь первым !')
print(f'На столе лежит {con} конфета')
while con > 0:
    if count == 0:
        step = int(input(f'{one} бери конфеты '))
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
        step = int(input(f'{two} бери конфеты '))
        if step > con:
            print('Столько конфет нет.Попробуй снова!')
        elif step > step_max:
            print(f'Максимальный ход {step_max} конфет.Попробуй снова!')
        else:
            con = con-step
            if con > 0:
               print(f'На кону {con}')
               count = 0

if count == 0:
    print(f'{one} ПОБЕДА!!!')
else:
    print(f'{two} ПОБЕДА!!!')
