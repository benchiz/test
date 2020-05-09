# Работа с файлами - запись (writing files)

with open('text.txt', 'a') as file:
    file.write('Hello')

# 2 - ой пример:
with open('text.txt', 'a') as file:
    file.write('Hello \n')
    file.write('world')

# Список
with open('text.txt', 'a') as file:
    file.writelines(['Hello', 'world'])

# С переносом строки
with open('text.txt', 'a') as file:
    file.writelines(['\nHello\n', 'world'])
