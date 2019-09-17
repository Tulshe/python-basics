# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
import random

numbers = []
n = int(input('Enter the desirable amount of numbers: '))
i = 0
while True:
    i += 1
    if i > n:
        break
    a = random.randint(-100, 100)
    numbers.append(a)
print(numbers)
