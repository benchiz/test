# Работа с файлами - чтение (read from file)

with open('text.txt', 'r') as file:
    text = file.read()

print(text)

# Построчный вывод
with open('text.txt', 'r') as file:
    for line in file:
        print(line)
# Список
with open('text.txt', 'r') as file:
    lines = file.readlines()

print(lines)
# Оптимизированный список(без \n)
with open('text.txt', 'r') as file:
    text = file.read()
    text = text.splitlines()

print(text)
