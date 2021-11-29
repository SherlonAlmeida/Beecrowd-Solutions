class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = {}
        self.visitados = []
        for i in range(self.V):
            self.grafo[i] = []
    
    def add_aresta(self, A, B):
        self.grafo[A].append(B) #A->B
        
    def dfs(self, v, tab):
        global flag
        indentacao = ""
        for i in range(tab):
            indentacao += "  " # 2 espacos em branco
        self.visitados.append(v)
        self.grafo[v].sort()
        for i in self.grafo[v]:
            flag = 1
            print(str(indentacao) + str(v) + "-" + str(i), end="")
            if not i in self.visitados:
                print(" pathR(G,%d)" % (i))
                self.dfs(i, tab+1)
            else:
                print("")

N = int(input())
flag = 0
for x in range(N):
    V,E = map(int, input().split())
    grafo = Grafo(V)    #Cria o Objeto Grafo
    for i in range(E):  #Adiciona as ligacoes
        A,B = map(int, input().split())
        grafo.add_aresta(A, B)
    
    print("Caso %d:" % (x+1))
    for i in grafo.grafo:
        if not i in grafo.visitados:
            tab = 1
            grafo.dfs(i, tab)
        if flag == 1:
            print("")
            flag = 0