tot = 0
for x in open('2023/day4/data.txt','r').readlines():
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