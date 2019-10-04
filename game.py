# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:
    def attack(self, defender):
        hit = self.damage / defender.armor
        return hit
    
    def hurt(self, hit):
        self.health = self.health - hit
        return self.health
    
    
class Player(Person):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.damage = 20
        self.armor = 1.4


class Enemy(Person):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.damage = 15
        self.armor = 1.2
        
        
class Fight(Person):
    def __init__(self, hitter, defender):
        super().__init__()
        self.hitter = Player()
        self.defender = Enemy()
    
    def fight(self):
        print(f'{self.hitter} starts fight with {self.hitter.health} health')
        print(f'{self.defender} starts fight with {self.defender.health} health \n')
        while True:
            print(f'{self.hitter} attacks {self.defender}')
            self.defender.hurt(self.hitter.attack(self.defender))
            print(f'{self.defender} has {self.defender.health} health \n')
            if self.defender.health <= 0:
                print(f'{self.hitter} won with {self.hitter.health} health left')
                break
            _ = self.hitter
            self.hitter = self.defender
            self.defender = _


hero = Player()
goblin = Enemy()
battle = Fight(hero, goblin)
battle.fight()
