import time
while True:
    N = int(input())
    if N == 0:
        break
    else:
        while True:
            A = list(map(int, input().split()))
            n_vagoes = len(A)
            total = len(A)
            B = []          #PILHA
            estacao = []    #PILHA
            flag = 0
            if (len(A)==1 and A[0]==0):
                break
            else:
                while True:
                    #time.sleep(1)
                    #print("A  : ", A, "B  : ", B, "Est: ", estacao, "VAGOES: ", n_vagoes)
                    if len(A)!=0:
                        if A[-1] == n_vagoes:
                            B.append(A[-1])     #Empilha    em B
                            del A[-1]           #Desempilha em A
                            n_vagoes -= 1
                        else:
                            if len(estacao) != 0:
                                if estacao[-1] == n_vagoes:
                                    B.append(estacao[-1])   #Empilha    em B
                                    del estacao[-1]         #Desempilha em E
                                    n_vagoes -= 1
                                else:
                                    estacao.append(A[-1])       #Empilha em E
                                    del A[-1]                   #Desempilha em A
                            else:
                                estacao.append(A[-1])       #Empilha em E
                                del A[-1]                   #Desempilha em A
                    else:
                        if len(estacao) != 0:
                            if estacao[-1] == n_vagoes:
                                B.append(estacao[-1])     #Empilha    em B
                                del estacao[-1]           #Desempilha em A
                                n_vagoes -= 1
                            else:
                                flag = 1
                                break
                        else:
                            break
                if flag == 1:
                    print("No")
                else:
                    print("Yes")
        print("")