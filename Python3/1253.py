def cesarDecipher(string, rotacao):
    saida = ""
    for i in string:
        index = alf.index(i)
        saida += alf[(index-rotacao)%len(alf)]
    print(saida)

alf = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
N = int(input())
for i in range(N):
    string = input()
    rotacao = int(input())
    cesarDecipher(string, rotacao)