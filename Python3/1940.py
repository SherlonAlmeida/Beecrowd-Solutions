j, r = tuple(map(int,input().split()))
points = list(map(int,input().split()))
jogadores = [None for x in range(j)]
for _ in range(j):
	jogadores[_] = sum(points[_::j])
	
maior = [0,0]
for i in range(len(jogadores)):
	if jogadores[i] >= maior[0]:
		maior = [jogadores[i], i +1]

print (maior[1])