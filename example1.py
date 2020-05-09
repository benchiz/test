login = input('Введите ваш логин: ')

if login == 'lgn':
    print('Хорошо!')
    password = input('Введите ваш пароль: ')

    if password == 'psswrd':
        print('Хорошо!')

    elif password == 'pswd':
        print('Окей!')

    else:
        print('Введён неверный пароль')

elif login == 'user':
    print('Хорошо user!')
    password = input('Введите ваш пароль: ')
    if password == 'psswrd':
        print('Хорошо!!!')

    elif password == 'pswd':
        print('Окей!!!')
    else:
        print('Введён неверный логин')

else:
    print('Введён неверный логин')

print('Программа завершена')
