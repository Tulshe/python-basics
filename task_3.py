# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов


def max_string():
    strings = []
    while True:
        string = input('Enter your data. Empty string will end input: ')
        strings.append(string)
        if string == '':
            break
    return max(strings, key=len)


print(max_string())
