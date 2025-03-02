from random import *

num = randint(1,100)
while True:
    try:
        choice = int(input("Guess the number: "))
        if choice == num:
            print("Congratulations you've got it.")
            break
        elif choice > num:
            print("Too high!")
        elif choice < num:
            print("Too low!")
    except ValueError:
        print("Invalid Input")

