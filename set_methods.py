# Методы работы со множеством set (set methods)

a = {1, 2, 3}
b = {2, 3, 4}
c = {3, 4, 5}

# update - Объединение
a.update(b, c)
print(a)
a = {1, 2, 3}
a |= b | c  # Аналогичный вариант метода update
print(a)
a = {1, 2, 3}

# Пересечение - intersection_update
a.intersection_update(b, c)
print(a)

a = {1, 2, 3}
a &= b & c  # Аналогичный вариант метода intersection_update
print(a)

a = {1, 2, 3}
# Вычитание - difference_update
a.difference_update(b, c)
print(a)
# {1} Является уникальной, среди всех множеств
a -= b | c  # Аналогичный вариант метода difference_update
print(a)

a = {1, 2, 3}
# symmetric_difference_update - Проверка 2 множеств и нахождение уникальных значений
a.symmetric_difference_update(b)
print(a)

a = {1, 2, 3}
a ^= b  # Аналогичный вариант метода symmetric_difference_update

# add - Добавление элемента во множество
a.add(2)
print(a)

# remove - удаление элемента из множества

a.remove(2)
print(a)

# discard - тоже самое что и remove, но если удалить элемент, которого нет во множестве, то исключения не будет

a.discard(1)
print(a)

# pop - удаляет рандомный элемент множества
print(a.pop())
print(a)

# clear - очищает множество
print(b)
b.clear()
print(b)
