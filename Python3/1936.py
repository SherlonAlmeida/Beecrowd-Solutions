import math

N = int(input())
N2 = N
soma = 0
cont = 0

while(soma != N):
	f = 1
	while(math.factorial(f) <= N2):
		f += 1
	soma += math.factorial(f-1)
	N2 -= math.factorial(f-1)
	cont +=1
	
print(cont)