with open("2023/day2/data.txt", "r") as file:
    total = 0
    for x in file:
        max_values = {'red': 0, 'blue': 0, 'green': 0}
        for y in x.strip().split(": ")[1].replace(";", ",").split(", "):
            amount, color = y.split()
            max_values[color] = max(max_values[color], int(amount))
        total += (max_values['red'] * max_values['green'] * max_values['blue'])
    print(total)