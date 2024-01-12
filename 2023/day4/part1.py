tot = 0
for x in open('FILEPATH.txt','r').readlines():
    wins, lots = x.split(":")[1].split("|")
    wins = wins.split()
    lots = lots.split()
    score = 0
    for y in wins:
        if y in lots:
            if score:
                score *= 2
            else:
                score = 1
    tot += score
print(tot)


# SHORT VERSION:
# print(sum(2**(len(set(a.split(":")[1].split("|")[0].split()) & set(a.split(":")[1].split("|")[1].split()))-1) if set(a.split(":")[1].split("|")[0].split()) & set(a.split(":")[1].split("|")[1].split()) else 0 for a in open('2023/day4/data.txt','r').readlines()))