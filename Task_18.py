# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1234 5
# 6 -> 5

import random
num = int(input('Введите количество элементов: '))
x = int(input('Введите проверочное число: '))
list_1 = []

for i in range(num):
    list_1.append(random.randint(0,20))

print(list_1)

dif = abs(x-list_1[0])
min = list_1[0]

for i in list_1:
    dif_2 = abs(x-i)
    if dif_2 < dif :
        min = i
print(min) 
