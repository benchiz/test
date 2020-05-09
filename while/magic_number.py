magic_number = int(input('Введите ваше число: '))

i = 0

while True:
    print(i)
    i += 1
    if i == magic_number:
        break

print('Your number is', i)