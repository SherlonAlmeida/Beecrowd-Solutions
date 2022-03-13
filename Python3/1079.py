N = int(input())        #Lendo a qualtidade de "Alunos"
pesos = [2.0, 3.0, 5.0] #Definindo os pesos para cada atividade

for i in range(N):
    notas = list(map(float, input().split()))
    quantidade_de_notas = len(notas) #Embora saibamos que eh 3, assim fica mais genérico/robusto
    soma = 0.0
    for i in range(quantidade_de_notas):
        soma += notas[i] * pesos[i]
    media = soma/10
    print("%.1f" % (media))