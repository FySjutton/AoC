with open("2023/day2/data.txt", "r") as file:
    total = 0
    for i, x in enumerate(file, 1):
        for y in x.split(": ")[1].replace(";", ",").split(", "):
            value, color = y.split()
            if {"red": 12, "green": 13, "blue": 14}[color.strip()] < int(value):
                break
        else:  
            total += i
    print(total)