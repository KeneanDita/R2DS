x = [1,3,4 ,56, 2, 32, 4, 34, 2]
print(sorted(x))

tup = ("Ken", "Avc", "krn", "amm")
print(sorted(tup))

#comparison doesn't work with int and str
#takes capital first and smalls in sorting them out

print(sorted(tup, key=lambda k: k[1]))
#lambda sort