# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# import random

# n = int(input('Укажите количество монеток на столе: '))
# orel = n - random.randint(1, n)
# reshka = n - orel

# if orel > reshka:
#     print(f'Меньше всего монет с РЕШКОЙ, следует перевернуть {reshka} монеты')
# elif reshka > orel:
#     print(f'Меньше всего монет с ОРЛОМ, следует перевернуть {orel} монеты')
# else: print(f'Монет поровно - "{orel}", можно выбрать любую')


# ВАРИАНТ 2
# import random

# print('Данная программа выведит минимальное количество монет, которое нужно перевернуть чтобы все монеты лежали одной стороной.')

# n = int(input('Укажите количество монеток на столе: '))
# orel = 0
# reshka = 0

# for i in range(n):
#     coinSide = random.randint(0, 1)
#     if coinSide == 1:
#         orel += 1
#     else: reshka += 1

# if orel > reshka:
#     print(f'Меньше всего монет с РЕШКОЙ, следует перевернуть {reshka} монеты')
# elif reshka > orel:
#     print(f'Меньше всего монет с ОРЛОМ, следует перевернуть {orel} монеты')
# else: print(f'Монет поровно - "{orel}", можно выбрать любую')






# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# S = int(input('Ведите сумму чисел: '))
# P = int(input('Ведите произведение чисел: '))

# for X in range(S):
#     for Y in range(P):
#         if S == X + Y and P == X * Y:
#             print(f'Первое число = {X} \nВторое число = {Y}')
#             break
#     else:
#         continue
#     break





# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# n = int(input('Введите предельное число: '))
# i = 0

# while i < n:
#     if 2**i <= n:
#         print(2**i)
#     i += 1