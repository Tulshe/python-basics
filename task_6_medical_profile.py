name = input('Enter your name: ')
surname = input('Enter your surname: ')
age = int(input('Enter your age: '))
weight = int(input('Enter your weight: '))

profile = [name, surname, age, weight]

if age < 30 and 50 < weight < 120:
    print(str(profile) + " - You're in a good shape!")
elif 30 < age < 40 and (weight < 50 or weight > 120):
    print(str(profile) + " - You should work on your body state!")
elif age > 40 and (weight < 50 or weight > 120):
    print(str(profile) + " - You need to visit a physician!")
