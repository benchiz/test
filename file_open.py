# Работа с файлами, открытие(file openning)

file = open('text.txt', 'r')

print(file.closed)
print(file.name)
print(file.mode)

file.close()

file = open('text.txt', 'r')

print(file.name)
print(file.mode)

file.close()

print(file.closed)
# После закрытия файла, будет True

# Создание файла
file = open('text.txt', 'w')

print(file.name)
print(file.mode)

file.close()

print(file.closed)

# Открытие файла на дозапись
file = open('text.txt', 'a')

print(file.name)
print(file.mode)

file.close()

print(file.closed)

# Комбинированные режимы открытия файла
# b - binary
file = open('text.txt', 'ab')  # wb, rb

print(file.name)
print(file.mode)

file.close()

print(file.closed)

# Комбинированный режим +
file = open('text.txt', 'a+') # a+, b+, r+, ab+, rb+, wb+

print(file.name)
print(file.mode)

file.close()

print(file.closed)

# Структура with, которая позволяет автоматически закрывать файл
with open('text.txt', 'w') as file:
    print(file.closed)

print(file.closed)
