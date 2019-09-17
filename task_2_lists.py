# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list_1 = ['member1', 'member2', 'member3', 'member4']
list_2 = ['member5', 'member1', 'member7', 'member3']

set1 = set(list_1)
set2 = set(list_2)
print(set1 - set2)
