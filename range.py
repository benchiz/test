# range - это в основном дополнение к  for

# 1-ый пример:
current_range = list(range(10))
print(current_range)

# 2-ой пример:
current_range = list(range(5, 10, 3))
print(current_range)

# 3-ый пример
for i in range(10):
    print(i)
# 4-ый пример
shopping_list = ['squash', 'tomato', 'milk', 'beer']

for i in range(len(shopping_list)):
    if shopping_list[i] == 'beer':
        shopping_list[i] = 'juice'
    print(shopping_list[i])
