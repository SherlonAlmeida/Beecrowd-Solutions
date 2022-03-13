N = 5
pares = 0
for i in range(N):
    x = int(input())
    if x % 2 == 0: #PAR
        pares += 1
print(pares, "valores pares")