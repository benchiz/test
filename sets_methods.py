# Методы работы со множествами set и frozenset (sets methods)
# Эти методы не изменяют множество

a = {1, 2, 3}
print(len(a))

print(1 in a)

b = {2, 3, 4}
c = {3, 4, 5}
print(a.union(b, c))  # union - объединение

result = a.union(b, c)

print(a | b | c)  # аналогичный вариант метода union

#  intersection - пересечение
print(a.intersection(b, c))
print(a & b & c)  # аналогичный вариант метода intersection

iresult = a.intersection(b, c)  # {3} - является множеством

# Вычитание или нахождение отличий - difference
print(a.difference(b, c))
print(a - b - c)  # аналогичный вариант метода difference

# symmetric_difference - возращает эл-ы, которые являются уникальными в 2 множествах
print(a.symmetric_difference(b))

# isdisjoint - проверка 2 множеств на уникальность
print(a.isdisjoint(b))

a = {1, 2}
b = {1, 2, 3}
print(a == b)
# issubset - Все эл-ы 1 множества принадлежат 2-ому, то будет True
print(a.issubset(b))
print(a <= b)  # аналогичный вариант метода issubset

# issuperset - Метод обратный методу issubset
print(b.issuperset(a))
print(b >= a)

# copy - Возвращает копию множества
print(a.copy())
