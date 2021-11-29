import copy
N = int(input()) # N competidores
K = int(input()) # Minimo classificados
jog = []
ganh = 0

for i in range(N):
	jog.append(int(input()))

jog.append(0)
	
jog.sort()
jog.reverse()

for i in range(K):
	ganh += 1
	if(i == K-1):
		while(True):
			if(jog[i] ==jog[i+1]):
				ganh += 1
				i += 1
			else:
				break
				
#print(jog)
print(ganh)