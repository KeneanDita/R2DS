choice = ""
while True:
    if choice == "n":
        break
    age = int(input("Age: "))
    try:
        if age < 0 or age >120:
            raise ValueError()
        else:
            print(f"You are {age} years old.")
    except ValueError:
        print("Invalid age Entered.")
    choice = input("Do you want to continue(Y/N)").lower()
