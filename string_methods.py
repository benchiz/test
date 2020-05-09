#string methods
string = 'Hello, world!'

string.find('Hello') #определение индекса каждой подстроки
# rfind - ищет не первый индекс, а правый с конца

string.index('Hello')
0
string.find('a')
-1
string.index('a') # будет ошибка

string.replace('Hell', 'Beautiful')
 # метод применяется лишь 1 раз, поэтому нужно переприсваивать переменную

string.split(' ') #разделяет слова по какому символу будет происходить разделение, используется в списках
current_list = string.split(' ')


string.upper()

string.lower()

string.capitalize()
# делает первый символ строки с большой буквы

string.title()
#делает каждое слово с большой буквы

string.count('o', 2)

string.strip()

#есть lstrip и rstrip - его аналоги
string.swapcase()

string = ', '.join(current_list)
>>> # метод join - объединяет все элементы в одну строку. В качестве аргумента используется список