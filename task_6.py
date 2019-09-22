# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.


def attack(attacker, attacked):
    damage = float(attacker.get('damage'))
    armor = float(attacked.get('armor'))
    hit = damage / armor
    return hit


def hurt(attacker, attacked):
    hit = attack(attacker, attacked)
    attacked['health'] = float(attacked['health'])
    attacked['health'] = round(float(attacked['health'] - hit), 1)
    
    
def write_file(entity):
    file = open(f'{entity.get("name")}.txt', 'w+', encoding='utf-8')
    for key, value in entity.items():
        string = f'{key} - {value}'
        file.write(string)
        file.write('\n')
    file.close()
    
    
def read_file(stats):
    entity = {}
    with open(stats) as file:
        for line in file:
            line = line.rstrip('\n')
            (key, value) = line.split(' - ')
            entity[key] = value
    for key in entity:
        print(key, entity[key])
    return entity


name = input('Enter your name: ')
player_base = {'name': name, 'health': 100, 'damage': 20, 'armor': 1.4}
enemy_base = {'name': 'goblin', 'health': 60, 'damage': 15, 'armor': 1.2}

write_file(player_base)
write_file(enemy_base)

player_read = read_file(f'{name}.txt')
enemy_read = read_file(f'{enemy_base.get("name")}.txt')

print('\n')
print(f'You attacked {enemy_read.get("name")}')

hitter = player_read
defender = enemy_read
while True:
    hurt(hitter, defender)
    print(f'{defender.get("name")} take {round(attack(hitter, defender), 1)} damage, health remain '
          f'{defender.get("health")}')
    if float(defender.get('health')) <= 0:
        break
    print('\n')
    print('Switch turns')
    _ = hitter
    hitter = defender
    defender = _
    
print(f'{defender.get("name")} is dead. {hitter.get("name")} won with {hitter.get("health")} hp')
