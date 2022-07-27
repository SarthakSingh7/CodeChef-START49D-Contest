for i in range(int(input())):
    tc = input().split()
    lis1 = [int(tc[0]),int(tc[1])] 
    lis2 = [int(tc[2]),int(tc[3])]
    out = max(lis1) + max(lis2)
    print(out)
