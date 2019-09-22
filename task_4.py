# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.
from typing import Dict


names = ['Vasya', 'Kolya', 'Petya', 'Ira', 'Natasha', 'Masha']
salaries = [20000, 30000, 35000, 600000, 32000, 25000]
employees = dict(zip(names, salaries))

file = open('salary.txt', 'w+', encoding='utf-8')
for key, value in employees.items():
    string = f'{key} - {value}'
    file.write(string)
    file.write('\n')
file.close()

employees_read = {}
with open('salary.txt') as file:
    for line in file:
        line = line.rstrip('\n')
        (key, value) = line.split(' - ')
        key = key.upper()
        value = int(value)
        if value > 500000:
            continue
        employees_read[key] = round(value - (value * 0.13))

for key in employees_read:
    print(key, employees_read[key])
