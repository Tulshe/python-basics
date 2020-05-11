import os


def create_dir():
    try:
        os.mkdir(input('Enter the name of new directory: '))
        print('Directory successfully created!')
    except FileExistsError:
        print('Such directory exists already. Enter another name: ')
        create_dir()
