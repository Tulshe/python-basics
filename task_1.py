# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

name = input('Enter your name: ')
age = input('Enter your age: ')
city = input('Enter the name of your city: ')


def info(name, age, city):
    string = f'{name}, {age} years old, lives in {city} city'
    return string


print(info(name, age, city))
