from random import *

while True:
    choice = input("Roll the Dice (y/n): ").lower()
    if choice == "y":
        a = (randint(1,6), randint(1,6))
        print(a)
    elif choice == "n":
        print("Thanks for playing the game.")
        break
    else:
        print("Invalid Choice!")