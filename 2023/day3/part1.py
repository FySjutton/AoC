lst = [x.replace("\n", "") for x in open("2023/day3/data.txt", "r").readlines()]
# print(lst)
# am = []
tot = 0
for i, x in enumerate(lst):
    for v, y in enumerate(x):
        if not y.isdigit() and y != ".":
            for p in ((-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                if not ((i == 0 and p[0] == -1) or ((i == (len(lst) - 1)) and p[0] == 1) or (v == 0 and p[1] == -1) or ((v == (len(x) - 1)) and p[1] == 1)):
                    if lst[i + p[0]][v + p[1]].isdigit():
                        new_int = lst[i + p[0]][v + p[1]]
                        a = 1
                        while True:
                            if lst[i + p[0]][v + p[1] + a].isdigit():
                                new_int += lst[i + p[0]][v + p[1]]
                            else:
                                break
                            a += 1
                        
                        a = 1
                        
                        while True:
                            if lst[i + p[0]][v + p[1] - a].isdigit():
                                new_int += lst[i + p[0]][v + p[1]]
                            else:
                                break
                            a += 1
                        tot += int(new_int)
print(tot)   
# print(len(am))