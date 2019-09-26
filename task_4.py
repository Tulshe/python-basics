#!/usr/bin/env python
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

import os
import shutil
import create
from my_delete import *
from open import *


def start():
    while True:
        print(f'You are now in {os.getcwd()}')
        choice = input('What do you want to do?\n'
                       '1. Open directory.\n'
                       '2. See containing files.\n'
                       '3. Remove this directory.\n'
                       '4. Remove directory.\n'
                       '5. Create directory\n'
                       '6. Exit.\n'
                       '\n'
                       'Your choice: ')
        if choice == '6':
            print('Good bye!')
            break
        options(choice)


def options(choice):
    if choice == '1':
        open_dir()
    elif choice == '2':
        contain()
    elif choice == '3':
        remove_this_dir()
    elif choice == '4':
        remove_dir()
    elif choice == '5':
        create.create_dir()
    else:
        print('Wrong input.')


start()
