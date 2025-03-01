def find_max(list):
    maximum = list[0]
    for num in list:
        if num > maximum:
            maximum = num
    return max