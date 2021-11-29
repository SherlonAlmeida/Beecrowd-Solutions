valor = int(input())
notas = [100,50,20,10,5,2,1]
total = [0,0,0,0,0,0,0]
sub = valor
atual = 0
while sub != 0:
    if sub - notas[atual] >= 0:
        sub -= notas[atual]
        total[atual] += 1
    else:
        atual += 1
print(valor)
for i in range(len(notas)):
    print("%d nota(s) de R$ %d,00" % (total[i], notas[i]))