while True:
    try:
        erro = 0
        pilha = []
        expressao = list(input())
        for i in range(len(expressao)):
            if (expressao[i] == '('): #Empilha
                pilha.append(expressao[i])
            elif (expressao[i] == ')'): #Desempilha
                if (len(pilha) > 0):
                    del pilha[-1]
                else:
                    erro = 1
                    break
        if (erro == 0) and (len(pilha) == 0):
            print("correct")
        else:
            print("incorrect")        
    except EOFError:
        break