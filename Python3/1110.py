while True:
    N = int(input())
    fila = []
    descartadas = []
    if N != 0:
        for i in range(N):
            fila.append(i+1)
        while (len(fila) >= 2):
            descartadas.append(fila[0]) #Adiciona Topo da fila em Descartadas
            del fila[0]                 #Remove o topo da fila
            topo = fila[0]              #Define o novo topo da fila
            del fila[0]                 #Remove o novo topo da fila
            fila.append(topo)           #E entao adiciona topo na base da fila
        string = "Discarded cards: "
        for i in range(len(descartadas)):
            if i < len(descartadas)-1:
                string += str(descartadas[i]) + ", "
            else:
                string += str(descartadas[i])
        print(string)
        print("Remaining card: %d" % (fila[-1])) #Imprime ultimo elemento da fila (Base da Fila)
    else:
        break