# Работа со списками(list methods)

shopping_list = ['squash', 'sugar', 'beer']
x = shopping_list.copy() # Копия списка


shopping_list.append('juice') # Добавление элемента в конец списка
print(shopping_list)

shopping_list.insert(4, 'bread') # Добавление элемента в опр. место
print(shopping_list)

shopping_list.remove('juice') # Удаление указанного и левого эл-а списка
print(shopping_list)

shopping_list.pop(2) # Удаление, но с указанием индекса в списке

print(shopping_list.index('squash')) # Индекс элемента в списке
print(shopping_list.count('beer'))  # Кол-во эл-ов в списке
print(shopping_list)

shopping_list.reverse() # Список в обратном направлении
print(shopping_list)

print(x)


shopping_list.extend(x) # Расширение списка, т.е. добавление 2-ого списка в 1-ый
print(shopping_list)

shopping_list.clear() # Очистка списка
print(shopping_list)