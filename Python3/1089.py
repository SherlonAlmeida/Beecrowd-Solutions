while True:
    N = int(input())
    if N == 0:
        break
    else:
        notas = list(map(int, input().split()))
        maxmin = 0 
        if (len(notas) == 2):
            if notas[0] == notas[1]:
                maxmin = 0
            else:
                maxmin = 2
        else:
            atual = "" #Inicializa
            if notas[-1] > notas[0]: #Decrescente
                atual = "decrescente"
            elif notas[-1] < notas[0]: #Crescente
                atual = "crescente"
            #print(notas)
            for i in range(len(notas)):
                if i == len(notas)-1:
                    if notas[-1] > notas[0]: #Decrescente
                        if atual == "crescente": #O contrario
                            maxmin += 1
                        atual = "decrescente"
                    elif notas[-1] < notas[0]: #Crescente
                        if atual == "decrescente": #O contrario
                            maxmin += 1
                        atual = "crescente"
                    #print(notas[-1], notas[0], atual)
                else:
                    if notas[i] > notas[i+1]: #Decrescente
                        if atual == "crescente": #O contrario
                            maxmin += 1
                        atual = "decrescente"
                    elif notas[i] < notas[i+1]: #Crescente
                        if atual == "decrescente": #O contrario
                            maxmin += 1
                        atual = "crescente"
                    #print(notas[i], notas[i+1], atual)
        print(maxmin)