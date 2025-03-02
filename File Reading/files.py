import json
import csv

file_path = "C:/Users/Ken/Videos/R2DS/File Reading/file.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Incorrect destination or file name")
except PermissionError:
    print("Not permitted.")


file_path = "C:/Users/Ken/Videos/R2DS/File Reading/file.json"
try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content["Job"])
except FileNotFoundError:
    print("File not found. Incorrect destination or file name")
except PermissionError:
    print("Not permitted.")


file_path = "C:/Users/Ken/Videos/R2DS/File Reading/file.csv"
try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])
except FileNotFoundError:
    print("File not found. Incorrect destination or file name")
except PermissionError:
    print("Not permitted.")
