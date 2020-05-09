# Неопределённое кол-во аргументов(flexible number of arguments)
def total_sum(*args):
    total = 0
    for i in args:
        total += i
    return total


print(total_sum(2))
print(total_sum(2, 5))
print(total_sum(2, 5, 1010))
