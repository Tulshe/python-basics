import os


def open_dir():
    try:
        os.chdir(input('Enter the name of directory'))
        print(f'Directory changed to{os.getcwd()}')
    except FileNotFoundError:
        print('No such directory. Try again.')
        open_dir()


def contain():
    print('This directory contain following directories and files:')
    print(os.listdir())
