aocdata = '2023/day4/data.txt'
lst = [[x[0].split(), x[1].split()] for x in [y.split(":")[1].split("|") for y in open(aocdata, "r").readlines()]]
des = {i: 1 for i in range(len(lst))}
tot = len(lst)
while len(des.keys()) > 0:
    edit_dic = {}
    for x in des.keys():
        for y in range(des[x]):
            wins = sum([1 for p in lst[x][0] if p in lst[x][1]])
            for q in range(1, wins + 1):
                if (x + q) < len(lst):
                    if (x + q) in edit_dic.keys():
                        edit_dic[x + q] += 1
                    else:
                        edit_dic[x + q] = 1
                    tot += 1
    des = edit_dic
print(tot)