data = open('2023/day4/data.txt', "r").readlines()

lst = []

for x in data:
    wins, lots = x.split(":")[1].split("|")
    lst.append([wins.split(), lots.split()])

tot = len(lst)
print(tot)
# for x in lst:
#     for y in x[0]:
#         if (y in x[1]):
#             tot += 1

des = {}
for i in range(len(lst)):
    des[i] = 1

while len(des.keys()) > 0:
    print("---")
    print(des)
    print(tt)
    tt = {}
    # print(tt)
    for x in des.keys():
        # print("A")
        # print(x)
        for y in range(des[x]):
            # print(y)
            if (x + y) < len(lst):
                # wins = 0
                # print(lst[x + y - 1])
                # print(x + y - 1)
                # print(lst[x + y][0])
                # print(lst[x + y][1])
                for p in lst[x + y][0]:
                    if p in lst[x + y][1]:
                        if (x + y) in tt.keys():
                            tt[x + y] += 1
                        else:
                            tt[x + y] = 1
                        tot += 1
    des = tt.copy()
    print(des)
    print(tot)

    # tt = {}
    # for x in des.keys():
    #     for i in range(des[x]):
    #         if (x + i + 1 < len(lst)):
    #             wins = 0
    #             for p in lst[x + i + 1][0]:
    #                 if p in lst[x + i + 1][1]:
    #                     wins += 1
    #             for h in range(wins):
    #                 if x + h + 1 in tt.keys():
    #                     tt[x + h + 1] += 1
    #                 else:
    #                     tt[x + h + 1] = 1
    #                 tot += 1
    # print(tt)
    # des = tt
print(tot)


# from collections import Counter
# tot = 0
# inst = []
# wwins = {}
# for i, x in enumerate(open('2023/day4/data.txt','r').readlines(), 1):
#     wins, lots = x.split(":")[1].split("|")
#     wins = wins.split()
#     lots = lots.split()
#     score = 0
#     for y in wins:
#         if y in lots:
#             score += 1
#     wwins[i] = score
#     for p in range(1, score):
#         inst.append(i + p)

# numbs = Counter(inst)
# test = 0
# for x in numbs.keys():
#     test += numbs[x]
# print(test)