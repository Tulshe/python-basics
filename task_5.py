# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.


def attack(attacker, attacked):
    damage = attacker.get('damage')
    health = attacked.get('health')
    attacked['health'] = health - damage


name = input('Enter your name: ')
player = {'name': name, 'health': 100, 'damage': 15}
enemy = {'name': 'goblin', 'health': 60, 'damage': 10}

print(player)
print(enemy)

print(f'You attacked {enemy.get("name")} ')
attack(player, enemy)
print(player)
print(enemy)

print(f'{enemy.get("name")} attacked you')
attack(enemy, player)
print(player)
print(enemy)


