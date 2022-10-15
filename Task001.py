#Напишите программу, удаляющую из текста все слова, содержащие "абв".
import os
clear=lambda:os.system('cls')
clear()

word = input('Введите текст: ')
data = word.split()
print(data)
res = list(filter(lambda e: 'абв' not in e.lower(), data))
print(res)

