# Словари (dict, dictionaries)
# В др. ЯП'ах это называется ассоциативным массивом
# ключ, значение
# Словарь - это неупорядоченная коллекция данных, поэтому найти значение по индексу невозможно

dictionary = {'first name':'Ivan', 'last name':'Ivanov'}
print(dictionary)
print(len(dictionary))

print(dictionary['first name'])

dictionary['age'] = 20
print(dictionary)