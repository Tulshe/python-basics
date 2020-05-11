import os
import shutil


def remove_this_dir():
    try:
        os.rmdir(os.getcwd())
        os.chdir("..")
    except OSError:
        print('This directory is not empty.')


def remove_dir():
    try:
        delete = input('Enter the name of directory to delete: ')
        os.rmdir(delete)
    except FileNotFoundError:
        print('There is no such directory.')
    except OSError:
        print('This directory is not empty.')
        answer = input('Do you wish to delete it anyway? Y/N')
        if answer == 'Y' or 'y':
            shutil.rmtree(delete, ignore_errors=True)
