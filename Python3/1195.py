class ArvoreBinaria:
    def __init__(self, chave, esquerda=None, direita=None):
        self.chave = chave
        self.esq = esquerda
        self.dir = direita
    
    def insere(self, raiz, no):
        if raiz == None:              #Insere no na raiz, caso nao haja raiz ainda
            raiz = no
        elif raiz.chave < no.chave:   #Insere ah direita
            if raiz.dir == None:
                raiz.dir = no
            else:
                self.insere(raiz.dir, no)
        else:                         #Insere ah esquerda
            if raiz.esq == None:
                raiz.esq = no
            else:
                self.insere(raiz.esq, no)
    
    def em_ordem(self, raiz): 
        if not raiz:
            return
        self.em_ordem(raiz.esq)                 #Visita Esquerda
        print(" %d" % (raiz.chave), end='')     #Visita atual (RAIZ)
        self.em_ordem(raiz.dir)                 #Visita Direita
    
    def pre_ordem(self, raiz): 
        if not raiz:
            return
        print(" %d" % (raiz.chave), end='')     #Visita atual (RAIZ)
        self.pre_ordem(raiz.esq)                #Visita Esquerda
        self.pre_ordem(raiz.dir)                #Visita Direita
        
    def pos_ordem(self, raiz): 
        if not raiz:
            return
        self.pos_ordem(raiz.esq)                #Visita Esquerda
        self.pos_ordem(raiz.dir)                #Visita Direita
        print(" %d" % (raiz.chave), end='')     #Visita atual (RAIZ)

Casos = int(input())
for i in range(Casos):
    N = int(input())
    nodos = list(map(int, input().split()))
    raiz = ArvoreBinaria(nodos[0])            #Cria Raiz
    for j in range(1, N):
        no = ArvoreBinaria(nodos[j])          #Cria o novo no
        raiz.insere(raiz, no)                 #Insere o novo no a partir da raiz
    
    print("Case %d:" % (i+1))
    print("Pre.:", end='')
    raiz.pre_ordem(raiz)
    print("")
    
    print("In..:", end='')
    raiz.em_ordem(raiz)
    print("")
    
    print("Post:", end='')
    raiz.pos_ordem(raiz)
    print("")
    
    print("")