# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N].
# Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1234 5
# 3 -> 1

import random
num = int(input('Введите количество элементов: '))
x = int(input('Введите проверочное число: '))
list_1 = []
count = 0

for i in range(num):
    list_1.append(random.randint(-5,5))

count = list_1.count(x)
print(list_1)

print(count if count != 0 else -1)