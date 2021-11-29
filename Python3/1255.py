N = int(input())
alf1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alf2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(N):
    frequencia = [0 for i in range(len(alf1))]
    frase = input()
    for j in range(len(frase)):
        if (frase[j] in alf1):
            frequencia[alf1.index(frase[j])] += 1
        elif (frase[j] in alf2):
            frequencia[alf2.index(frase[j])] += 1
    maximos = frequencia.count(max(frequencia))
    if maximos == 1:
        index = frequencia.index(max(frequencia))
        print(alf1[index])
    else:
        string = []
        for j in range(maximos):
            index = frequencia.index(max(frequencia))
            string.append(alf1[index])
            frequencia[index] = -1
        string.sort()
        saida = ""
        for j in range(len(string)):
            saida += string[j]
        print(saida)