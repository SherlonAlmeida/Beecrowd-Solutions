while True:
    A,C = map(int, input().split())
    if (A==C==0):
        break
    else:
        bloco = list(map(int, input().split()))
        laser = 0 #Inicializa
        for i in range(C):
            if i!=0:
                if (bloco[i-1] > bloco[i]):
                    laser += (bloco[i-1]-bloco[i])
            else:
                laser += A-bloco[i]
        print(laser)