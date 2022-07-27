for i in range(int(input())):
    tc = input().split()
    A = int(tc[0])
    B = int(tc[1])
    C = int(tc[2])
    # if A == 0 or B == 0 or C == 0 or A > 10 or B > 10 or C > 1:
    #      print('NO')
    if (A == B and B == C and C == A):
        print('YES')
    elif A == B and B != C and A != C and A < C:      # A = B,  A < C because the non repeated number should be gretaer than the repeated number
        print('YES')
    elif A != B and B == C and A != C and A > C:      # B = C 
        print('YES')
    elif A != B and A == C and B != C and B > A:      # C = A
        print('YES')
    elif (A != B and B!= C and C != A):
        print('NO')
    else:
        print('NO')
