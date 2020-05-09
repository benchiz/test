import random as rnd


shopping_list = ['tomato', 'squash', 'milk']

print(rnd.choice(shopping_list))

# Если из модуля нужно всего лишь несколько ф-ий
from random import choice as ch

shopping_list = ['tomato', 'squash', 'milk']

print(ch(shopping_list))

# Если нужно импортировать сразу все ф-ии
from random import * # не рекомендуется

shopping_list = ['tomato', 'squash', 'milk']

print(choice(shopping_list))