from random import *
#
# for i in range(3):
#     print(random())
#
# for i in range(3):
#     print(randint(10,13))
#
# members = ["Atne", "Ken", "Mesfine"]
# leader = choice(members)
# print(leader)
class Dice:
    def roll(self):
        roll = (randint(1, 6), randint(1, 6))
        return roll

roll1 = Dice()
print(roll1.roll())

values = [1,2,3,4,5,6]
rol = (choice(values), choice(values))
print(rol)

rolls = (randint(1,6), randint(1,6))
print(rolls)
