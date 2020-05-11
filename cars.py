# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:
    def __init__(self, spd, nm, clr, plc):
        self.speed = int(spd)
        self.color = str(clr)
        self.name = str(nm)
        self.max_speed = int
        self.is_police = str(plc)

    def __bool__(self):
        if self.is_police == 'police':
            return True
        else:
            return False
     
    def go(self):
        if self.speed <= self.max_speed:
            print(f'{self.name} goes straight at {self.speed} km/h')
        else:
            print("This car can't go so fast.")
            
    def stop(self):
        print(f'{self.name} stopped')
        
    def turn(self, dir):
        direction = dir
        print(f'{self.name} turns {direction}')


class TownCar(Car):
    def __init__(self, spd, mn, clr, plc):
        super().__init__(spd, mn, clr, plc)
        self.max_speed = 120
      

class SportCar(Car):
    def __init__(self, spd, mn, clr, plc):
        super().__init__(spd, mn, clr, plc)
        self.max_speed = 200
        
        
class WorkCar(Car):
    def __init__(self, spd, mn, clr, plc):
        super().__init__(spd, mn, clr, plc)
        self.max_speed = 60
        self.color = 'brown'


class PoliceCar(Car):
    def __init__(self, spd, mn, clr, plc):
        super().__init__(spd, mn, clr, plc)
        self.max_speed = 220
        self.color = 'blue and white'
