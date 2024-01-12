lst = [x.replace("\n", "") for x in open("FILEPATH.txt", "r").readlines()]
tot = 0
for i, x in enumerate(lst):
    for v, y in enumerate(x):
        if y == "*":
            ind, nmbs = [], []
            for p in ((-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                row = lst[i + p[0]]
                if row[v + p[1]].isdigit() and (i + p[0], v + p[1]) not in ind:
                    new_int = row[v + p[1]]
                    for dir in (1, -1):
                        for l in range(1, len(row) - v - 1):
                            cur_ind = v + p[1] + dir * l
                            if row[cur_ind].isdigit():
                                ind.append((i + p[0], cur_ind))
                                new_int = new_int + row[cur_ind] if dir > 0 else row[cur_ind] + new_int
                            else:
                                break
                    nmbs.append(int(new_int))
            if (len(nmbs) == 2):
                tot += nmbs[0] * nmbs[1]
print(tot)