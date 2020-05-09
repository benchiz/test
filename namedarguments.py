# named arguments 

def employee_card(name, age, sex):
    card = []
    card.append(name)
    card.append(age)
    card.append(sex)
    return card


manager = employee_card('Jack', age=27, sex='M') # named arguments
print('Name:', manager[0])
print('Age:', manager[1])
print('Sex:', manager[2])