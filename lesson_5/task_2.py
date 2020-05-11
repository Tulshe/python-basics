# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os


print([i for i in os.listdir() if os.path.isdir(i)])
