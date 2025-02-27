import pprint
from sgpt import printer

#Flattening a matrix(lists of lists)
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flattened = [num for row in matrix for num in row]
print(flattened)

#Comprehending strings on if else
categories = ["Even" if x % 2==0 else "Odd" for x in range(10)]
print(categories)

#Comprehension with function
def cube(x):
    return x**3
result = [cube(num) for num in range(10)]
print(result)

#Dictionary Comprehension
pair = [('a',1 ),('b', 2) ]
result = {k:v for k,v in pair}
print(result)

#Removing duplicates while applying functions (Set Comprehension)
list = [1,2,3,4,4,4,2,5,6,5,3]
result = {x**3 for x in list}
print(result)

#Generator Comprehension
suma = sum(x**2 for x in range(10))
print(suma)
