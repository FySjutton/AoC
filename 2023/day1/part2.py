import os
data = open(os.getcwd() + "/2023/day1/data.txt", "r")
get_number, total = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}, 0
for x in data.readlines():
    letter_str, number_str = "", ""
    for y in x:
        if y.isdigit():
            number_str += y
        else:
            letter_str += y
        for p in get_number.keys():
            if (p in letter_str):
                number_str += get_number[p]
                letter_str = p[-1]
    total += int(number_str[0] + number_str[-1])
print(total)