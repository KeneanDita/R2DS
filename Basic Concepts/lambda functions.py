num = [1,2,3,4,5,6,7,8,9,10]

square = list(map(lambda x: x**2, num))
print(square)

even = list(filter(lambda x: x %2==0, num))
print(even)

value = [(1, "b", "value"),(3,"a","kenean"),(2,"c","atinaf")]
sort = sorted(value, key=lambda x:x[1])
print(sort)