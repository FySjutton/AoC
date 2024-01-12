total = 0
for x in open("FILEPATH.txt", "r").readlines():
    ny_kod = "".join(y for y in x if y.isdigit())
    total += int(ny_kod[0] + ny_kod[-1])
print(total)