entrada = input()
vogais = ['a','e','i','o','u']

prim = []
seg = []

for i in range(len(entrada)):
	if(entrada[i] in vogais):
		prim.append(entrada[i])
		
seg = prim[::-1]

if(prim == seg):
	print("S")
else:
	print("N")