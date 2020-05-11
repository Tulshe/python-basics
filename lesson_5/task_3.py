# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


import shutil
import sys


shutil.copyfile(src='task_3.py', dst='task_3_copy.py')


# for i in range(sys.maxsize**10):
#     shutil.copyfile(src='task_3.py', dst=f'task_3_copy{i}.py')
#Если я правильно понял таким скриптом можно засрать весь компьютер мусорными файлами до нерабочего состояния.
# Запускать я его, конечно же, не стал.
