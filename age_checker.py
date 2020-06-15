# Обработка исключений(handling exceptions)

age = input('Enter your age: ')

if age >= 21:
    print('Welcome!')

else:
    print('You must be at least 21!')

# Пример:
try:
    age = int(input('Enter your age: '))

except:
    print('Error')

if age >= 21:
    print('Welcome!')

else:
    print('You must be at least 21!')

# 2 - ой пример:
# Обработка исключений(handling exceptions)

try:
    age = int(input('Enter your age: '))


except ValueError as error:
    print('Error')
    print(error)

if age >= 21:
    print('Welcome!')

else:
    print('You must be at least 21!')


# 3 - ий пример:
# Обработка исключений(handling exceptions)

while True:

    try:
        age = int(input('Enter your age: '))

    except ValueError as error:
        print('Error')
        print(error)
        continue

    if age >= 21:
        print('Welcome!')

    else:
        print('You must be at least 21!')

    break

# 2 - ой способ:
while True:

    try:
        age = int(input('Enter your age: '))

    except ValueError as error:
        print('Error')
        print(error)
    else:
        break

if age >= 21:
    print('Welcome!')

else:
    print('You must be at least 21!')

# finally
while True:

    try:
        age = int(input('Enter your age: '))

    except ValueError as error:
        print('Error')
        print(error)
    else:
        break
    finally:
        print('Thanks anyway!')

if age >= 21:
    print('Welcome!')

else:
    print('You must be at least 21!')
