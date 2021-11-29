X = int(input())
percorre = 0
lista = []
listastring = []

for i in range(X):
    adicionar = []
    i = input()
    a = i.split()
    for j in range(len(a)):
        adicionar.append(a[j])
        adicionar.reverse()
        adicionar.sort(key=len)
        adicionar.reverse()
    add = ' '.join(adicionar)
    lista.append(add)
for z in range(len(lista)):
    inserir = ''.join(lista[z])
    print(inserir)