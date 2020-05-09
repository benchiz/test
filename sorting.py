# list sorting. Методы sort и sorted(Сортировка списков)

# 1 - ый пример:
shopping_list = ['bread', 'milk', 'squash']

def sort_by_first_letter(i):
    return i[0]

shopping_list.sort(key=sort_by_first_letter)

print(shopping_list)

# 2 - ой пример:
shopping_list = ['bread', 'milk', 'squash']

shopping_list.sort()

print(shopping_list)

# 3 - ий пример:
shopping_list = ['bread', 'milk', 'squash']

shopping_list.sort(reverse=True)

print(shopping_list)

# 4 - ый пример:
shopping_list = ['bread', 'milk', 'squash']

def sort_by_first_letter(i):
    return i[-1]

shopping_list.sort(key=sort_by_first_letter)

print(shopping_list)

# 5 - ый пример:
shopping_list = ['bread', 'milk', 'squashes']

def sort_by_first_letter(i):
    return len(i)

shopping_list.sort(key=sort_by_first_letter)

print(shopping_list)

# 6 - ой пример:
shopping_list = ['bread', 'milk', 'squashes']

def sort_by_first_letter(i):
    return len(i)

shopping_list.sort(key=sort_by_first_letter, reverse=True)

print(shopping_list)

# Метод sort изменяет сам список, а не возвращает отсортированную копию
# Метод sorted возвращает отсортированную копию списка

# 7 - ой пример:
shopping_list = ['bread', 'milk', 'squashes']

sorted_list = sorted(shopping_list)

print(shopping_list)
print(sorted_list)