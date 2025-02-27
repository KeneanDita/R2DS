#no conditions
values = [x for x in range(20)]
print(values)

#one if statment
odd = [n for n in range(50) if n %2 ==1]
print(odd)

#multiple if conditions on top of each other
names = ['Kenean', 'Atinaf', 'Mesfin', 'Ken', 'Mean',]
validNames = [
    name for name in names
    if len(name) >= 5
    if name[0] == 'K' or 'M' or 'A'
    if name[-1] == 'n' or 'f'
]
print(validNames)

