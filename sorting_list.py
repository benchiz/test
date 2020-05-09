shopping_list = ['bread', 'milk', 'squash']

def sort_by_first_letter(i):
    return i[0]

shopping_list.sort(key=sort_by_first_letter)

print(shopping_list)
