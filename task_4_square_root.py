# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь

numbers = [4, 6, 9, 15, 17, 25, 36, 41, 64]
numbers_roots = []

for num in numbers:
    a = num ** 0.5
    if a.is_integer():
        numbers_roots.append(a)
print(numbers_roots)
