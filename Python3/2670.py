A = []
for _ in range(3):
	A.append(int(input()))
	
c1 = A[1]*2 + A[2]*4 #Maquina no andar 0
c2 = A[0]*2 + A[2]*2 #Maquina no andar 1
c3 = A[0]*4 + A[1]*2 #Maquina no andar 2
res = min(c1,c2,c3)
print(res)