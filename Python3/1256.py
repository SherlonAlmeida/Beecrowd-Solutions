def funcao_hash(x, TAM):
    return x % TAM

N = int(input())
for i in range(N):
    memoria = {}
    M,C = map(int, input().split())
    CHAVES = list(map(int, input().split()))
    
    for j in range(M):
        memoria[j] = []
    
    for j in range(C):
        endereco = funcao_hash(CHAVES[j], M)
        memoria[endereco].append(CHAVES[j])
    
    for j in range(len(memoria)):
        saida = ""
        saida += str(j) + " -> "
        for k in range(len(memoria[j])):
            saida += str(memoria[j][k]) + " -> "
        saida += "\\"
        print(saida)
    if i < N-1:
        print("")