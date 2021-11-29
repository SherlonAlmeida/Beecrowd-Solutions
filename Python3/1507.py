N = int(input())
for i in range(N):
    S = list(input())
    Q = int(input())
    for j in range(Q):
        C = list(input())
        lenS = len(S);
        total = len(C)
        cont = 0
        flag = 0
        for k in range(lenS):
            if (cont == total):
                flag = 1
                break
            if (S[k] == C[0]):
                del C[0]
                cont += 1
        if (flag == 1) or (cont==total):
            print("Yes")
        else:
            print("No")