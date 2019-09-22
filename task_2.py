# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них


def max_number(num_1, num_2, num_3):
    max = num_1
    if num_2 > max:
        max = num_2
        if num_3 > max:
            max = num_3
    return max


num_1 = input('Enter number 1: ')
num_2 = input('Enter number 2: ')
num_3 = input('Enter number 3: ')

print(max_number(num_1, num_2, num_3))
