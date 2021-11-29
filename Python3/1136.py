while True:
    N,B = map(int, input().split())
    R = [ i for i in range(1, N+1)]
    if (N==0) and (B==0):
        break
    else:
        carta = list(map(int, input().split()))
        for j in range(B):
            for k in range(j, B):
                if (j!=k):
                    X = abs(carta[j]-carta[k])
                    if X in R:
                        R.remove(X)
    if len(R) == 0:
        print("Y")
    else:
        print("N")