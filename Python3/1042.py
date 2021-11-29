vetorInicial = list(map(int, input().split()))
vetorOrdenado = [vetorInicial[i] for i in range(len(vetorInicial))]
vetorOrdenado.sort()
for ordem in vetorOrdenado:
    print(ordem)
print("")
for lidos in vetorInicial:
    print(lidos)