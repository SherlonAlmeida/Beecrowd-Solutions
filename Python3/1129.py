alt = ['A', 'B', 'C', 'D', 'E']
while True:
    try:
        N = int(input())
        if N > 0:
            Matriz =  [[-1 for i in range(5)] for j in range(N)]
            for i in range(N):
                Matriz[i] = list(map(int, input().split()))
            for i in range(len(Matriz)):
                marcadas = 0
                indice = -1
                for j in range(5):
                    if Matriz[i][j] <= 127:
                        marcadas += 1
                        indice = j
                if (marcadas == 0) or (marcadas > 1):
                    print("*")
                else:
                    print(alt[indice])
    except EOFError:
        break