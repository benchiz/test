# dict iteration(Перебор словарей)

person = {'first name': 'Jack', 'last name': 'White', 'age': '25'}

for i in person:
    print(i)

# 2 - ой пример(значения):
person = {'first name': 'Jack', 'last name': 'White', 'age': '25'}

for i in person:
    print(person[i])

# 3 - ий пример:
person = {'first name': 'Jack', 'last name': 'White', 'age': '25'}

for i in person:
    print(i, person[i])

'''
Метод items содержит в этом случае объект dict_items
в котором находятся кортежи, имеющие ключ и значение.
for i, j(для ключа и значения)
'''
for i, j in person.items():
	print(i, j)

# 2 - ой метод keys
for i in person.keys():
	print(i)

# Основной метод при переборе словарей - values
for i in person.values():
	print(i)