# this program changes numerical number into words
phone = input("Phone: ")

numbers = { 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"Six",
            7:"seven", 8:"eight", 9:"nine", 0:"zero"
}

output = ""
for digit in phone:
    output += numbers.get(int(digit) ,digit) + " "

print(output)