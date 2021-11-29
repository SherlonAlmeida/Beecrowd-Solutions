class ArvoreBinaria:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None
 
def constroi_arvore(infixo, prefixo, inicio, fim):
    if (inicio > fim):
        return None
    aux = ArvoreBinaria(prefixo[constroi_arvore.Indice])
    constroi_arvore.Indice += 1
    if inicio == fim :
        return aux
    ind = busca_indice(infixo, inicio, fim, aux.valor)
    aux.esq = constroi_arvore(infixo, prefixo, inicio, ind-1)
    aux.dir = constroi_arvore(infixo, prefixo, ind+1, fim)
    return aux
 
def busca_indice(infixo, inicio, fim, valor):
    for i in range(inicio, fim+1):
        if infixo[i] == valor:
            return i
 
def pos_ordem(raiz):
    if raiz == None:
        return
    pos_ordem(raiz.esq)                    #Visita Esquerda 
    pos_ordem(raiz.dir)                    #Visita Direita
    print("%c" % (raiz.valor), end='')     #Visita atual (RAIZ)
     
N = int(input())
for i in range(N):
    letras,prefixo,infixo = input().split()
    letras = int(letras)
    infixo = list(infixo)
    prefixo = list(prefixo)
    constroi_arvore.Indice = 0
    raiz = constroi_arvore(infixo, prefixo, 0, len(infixo)-1)
    pos_ordem(raiz)
    print("")