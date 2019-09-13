number = int(input('Enter a number:'))
while number < 0 or number > 10:
    number = int(input('Number must be from 0 to 10. Enter new number:'))

print("Number's square is: " + str(number**2))
