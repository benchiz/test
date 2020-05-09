# dict methods(Методы работы со словарями)

person = {}
print(person.fromkeys(('first name', 'last name')))

person = person.fromkeys(('first name', 'last name'), 'Jack')
print(person)

print(person.get('first name'))
print(person.get('age', 20))

print(person.pop('first name'))
print(person)

# Удаление рандомной пары ключ, значение
print((person.popitem()))
print(person)

person.setdefault('first name', 'Jack')
person.setdefault('last name', 'White')
print(person)

person.update({'age': 25, 'sex': 'm'})
print(person)

person.copy()

person_one = person.copy()
print(person_one)

person.clear()
print(person)