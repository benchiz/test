# Генерация - вызов исключений(raise exception)

while True:

    try:
        age = int(input('Enter your age: '))

        if age < 0:
            raise ValueError('Incorrect age!')

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
