for i in range(int(input())):
    N = int(input())  # number of buttons 
    S = input()
    R = input()
    count = 0
    for i in range(N):
        if S == R:
            state = 1
        if S[i] != R[i]:
            count = count + 1
            if count%2 == 0:
                state = 1
            elif count%2 != 0:
                state = 0
    print(state)  
