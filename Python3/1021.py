valor = float(input())
dinheiro = [100.0,50.0,20.0,10.0,5.0,2.0,1.0,0.50,0.25,0.10,0.05,0.01]
total = [0,0,0,0,0,0,0,0,0,0,0,0]
atual = 0
while (valor != 0):
    if (valor - dinheiro[atual] >= 0):
        valor = round(valor - dinheiro[atual], 2)
        total[atual] += 1
    else:
        atual += 1

print("NOTAS:")
for i in range(0, 6):
    print("%d nota(s) de R$ %.2f" % (total[i], dinheiro[i]))
print("MOEDAS:")
for i in range(6, len(dinheiro)):
    print("%d moeda(s) de R$ %.2f" % (total[i], dinheiro[i]))