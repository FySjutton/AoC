print(sum(i for i, x in enumerate(open("FILEPATH.txt", "r").readlines(), 1)
    if all({"red": 12, "green": 13, "blue": 14}[y.split()[1]] >= int(y.split()[0])
        for y in x.split(": ")[1].replace(";", ",").split(", "))))