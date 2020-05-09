# Область видимости переменных(variable scope)

# 1-ый пример

message = 'Hello!'
def tomato():
	print(message)


def squash():
	print(message)

print(message)
tomato()
squash()

# 2-ой пример

def tomato():
	message = 'Hello!'
	print(message)


def squash():
	print(message)

print(message)
tomato()
squash()
# Будет ошибка, как так переменная message указана только в ф-ии 'tomato' и является локальной
# P.S. Переменные бывают глобальные и локальные	