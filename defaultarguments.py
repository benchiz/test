# default arguments
def employee_card(name='unknown', age='unknown', sex='unknown'):
    card = []
    card.append(name)
    card.append(age)
    card.append(sex)
    return card


manager = employee_card(name='Jack', sex='M')
print('Name:', manager[0])
print('Age:', manager[1])
print('Sex:', manager[2])