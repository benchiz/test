# Создание модуля(create module)

def welcome():
    name = input('Your name: ')
    print('Welcome', name)

print('My module')

# Отдельная программа 

import example1 as wlc

wlc.welcome()
print('Hey it\'s working')

# Если нужно, чтобы программа работала как самостоятельная программа

def welcome():
    name = input('Your name: ')
    print('Welcome', name)


if __name__ == '__main__':
    print('My module')

# 2 - ой вариант
# Отдельная программа
from example1 import welcome

welcome()
print('Hey it\'s working')

# Основная программа
def welcome():
    name = input('Your name: ')
    print('Welcome', name)


print('My module')
