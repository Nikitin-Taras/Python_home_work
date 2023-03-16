# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))

solution_exists = 0
for i in range(s):
    if i * (s - i) == p:
        print(f'Петя загадал числа {i} и {s-i}')
        solution_exists = 1
        break
if solution_exists == 0: 
    print('Таких натуральных чисел нет!') 

print('Некорректный ввод. Попробуйте еще раз!')