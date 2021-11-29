Repeticoes = 0
Inter = 0
Gremio = 0
Empate = 0

Repeticoes += 1
inter,gremio = map(int, input().split())
if inter > gremio:
    Inter += 1
elif inter < gremio:
    Gremio += 1
elif inter == gremio:
    Empate += 1
    
while True:
    N = int(input())
    if N == 1:
        inter,gremio = map(int, input().split())
        Repeticoes += 1
        if inter > gremio:
            Inter += 1
        elif inter < gremio:
            Gremio += 1
        elif inter == gremio:
            Empate += 1
    else:
        break

for i in range(Repeticoes):
    print("Novo grenal (1-sim 2-nao)")
    
print("%d grenais" % (Repeticoes))
print("Inter:%d" % (Inter))
print("Gremio:%d" % (Gremio))
print("Empates:%d" % (Empate))
if Gremio == Inter:
    print("Nao houve vencedor")
elif Inter > Gremio:
    print("Inter venceu mais")
elif Gremio > Inter:
    print("Gremio venceu mais")