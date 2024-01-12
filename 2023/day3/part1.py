lst = [x.replace("\n", "") for x in open("FILEPATH.txt", "r").readlines()]
tot, used_nbrs = 0, []
for i, x in enumerate(lst):
    for v, y in enumerate(x):
        if not y.isdigit() and y != ".":
            for p in ((-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                row = lst[i + p[0]]
                if row[v + p[1]].isdigit() and (i + p[0], v + p[1]) not in used_nbrs:
                    new_int = row[v + p[1]]
                    for dir in (1, -1):
                        for l in range(1, len(row) - v - 1):
                            cur_ind = v + p[1] + dir * l
                            if row[cur_ind].isdigit():
                                used_nbrs.append((i + p[0], cur_ind))
                                new_int = new_int + row[cur_ind] if dir > 0 else row[cur_ind] + new_int
                            else:
                                break
                    tot += int(new_int)
print(tot)