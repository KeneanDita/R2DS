from pandas.core.dtypes.cast import maybe_upcast_numeric_to_64bit

numbers = [1, 2, 5, 3, 1, 5, 5, 3]
# removedNum = []
# for i,num in enumerate(numbers):
#     if i >= 1:
#         if num not in removedNum:
#             removedNum.append(num)
#     else :
#         removedNum.append(num)
#
# print(removedNum)

removedNum = []
for num in numbers:
    if num not in removedNum:
        removedNum.append(num)
print(removedNum)

