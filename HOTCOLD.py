out = []
for i in range(int(input())):
    t = int(input())  # value of temp 
    if t <= 20:
        cli = "COLD"
        out.append(cli)
    elif t > 20:
        cli = "HOT"
        out.append(cli)
for i in out:
    print(i)
