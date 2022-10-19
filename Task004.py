#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
from base64 import encode
from itertools import count
import os
clear=lambda: os.system('cls')
clear()

def encode(data): 
    encoding= ' '
    count=1
    for j in range(len(data)-1):
        if data[j]==data[j+1]:
            count+=1 
        else:
            encoding=encoding+str(count)+data[j]
            count=1
    if count > 1 or (data[len(data)-2] != data[-1]):
        encoding = encoding + str(count) + data[-1]       
    return encoding
  
s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {encode(s)}")


def decode(data):
    number = ''
    decoding = ''
    for i in range(len(data)):
        if not data[i].isalpha():
            number += data[i]
        else:
            decoding = decoding + data[i] * int(number)
            number = ''
    return decoding

s=input('Ведите текст для дешивровки: ')
print(decode(s))