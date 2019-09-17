# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

fruits = ['apple', 'banana', 'kiwi', 'watermelon']

max = len(fruits[0])
for fruit in fruits:
    a = len(fruit)
    if a > max:
        max = a

i = 1
for fruit in fruits:
    this = len(fruit)
    diff = max - this
    space = ' '*diff
    print(i, space, fruit)
    i = i + 1
