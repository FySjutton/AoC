print(sum(
    [q[0] * q[1] * q[2] for q in 
        [[max(s) for s in v] for v in
            [[[int(y.split()[0]) 
                for y in x.strip().split(": ")[1].replace(";", ",").split(", ") 
                if y.split()[1] == p] for p in ["red", "blue", "green"]] 
                for x in open("2023/day2/data.txt", "r").readlines()]]]))