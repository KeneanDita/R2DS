from functools import reduce

num = [1,2,3,56,4,5,6,7,8,9,10]
sum = reduce(lambda x, y: x+y, num)
print(sum)


max = reduce(lambda x,y: x if x>y else y, num)
print(max)


comp = {x:(lambda x:x**2)(x) for x in range(5)}
print(comp)