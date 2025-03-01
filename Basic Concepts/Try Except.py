while True:
    try:
        age = int(input("Age: "))
        print(age)
        break
    except ZeroDivisionError:
        print("Age can't be zero")
    except ValueError:
        print("Invalid Entry")