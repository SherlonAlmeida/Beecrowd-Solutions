chave = input()
linhas = int(input())
alf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
vog = ['a','e','i','o','u']
for palavra in range(linhas):
    msg = input().split(" ")
    cont = 0
    saida = ""
    for i in range(len(msg)):
        msg[i] = list(msg[i])
        if msg[i][0] not in vog:
            for j in range(len(msg[i])):
                x = alf.index(chave[(cont)%len(chave)])
                y = alf.index(msg[i][j])
                #print(alf[x], alf[y])
                saida += alf[(x+y)%len(alf)]
                cont += 1
        else:
            for j in range(len(msg[i])):
                saida += msg[i][j]
        if i < (len(msg)-1):
            saida += " "
    print(saida)