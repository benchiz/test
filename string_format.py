# Форматирование строк. Метод format(string format)

# 1 - ый пример: 
first_name = 'Jack'
last_name = 'Jackson'

print('My name is {}. My last name is {}.'.format(first_name, last_name))

# 2 - ой пример:
print('My name is {0}. My last name is {1}.'.format(first_name, last_name))

# 3 - ий пример:
print('My name is {name}. My last name is {surname}.'.format(name=first_name, surname=last_name))