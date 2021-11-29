while True:
    N,M = map(int, input().split())
    if (N==0) and (M==0):
        break
    #fila = [i+1 for i in range(N)]
    pulo = 1    #Pulo atual
    pedra = 0   #Pedra atual
    premio = M  #Onde esta o premio
    #print("Premio: ", premio, end=" ")
    if premio > 34:
        print("Let me try!")
    else:
        while True:
            #print(pedra, end=" ")
            salto = (2*pulo)-1
            if pedra == premio:
                print("Let me try!")
                break
            elif (pedra > premio): #Se o sapo esta na direita
                if (pedra-salto) >= 1:
                    pedra -= salto #Vai para esquerda
                elif (pedra+salto) <= N:
                    pedra += salto #Vai para esquerda
                else:
                    print("Don't make fun of me!")
                    break
            elif (pedra < premio): #Se o sapo esta na esquerda
                if (pedra+salto) <= N:
                    pedra += salto #Vai para direita
                elif (pedra-salto) >= 1:
                    pedra -= salto #Vai para esquerda
                else:
                    print("Don't make fun of me!")
                    break
            pulo += 1