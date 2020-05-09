# Списковое выражение(генератор списков) list comprehension 
# 1-ый пример
numbers = []

for i in range(8):
	numbers.append[i] # append - добавление элемента

print(numbers)

# 2-ой пример
numbers = [i for i in range(8)]

print(numbers)

numbers = [i*2 for i in range(8)]

print(numbers)

# + условие
numbers = [i*2 for i in range(8) if i % 2 == 0]

print(numbers)