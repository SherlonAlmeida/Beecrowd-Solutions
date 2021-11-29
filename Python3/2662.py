N = int(input())
d = dict()
escala = ['do','do#','re','re#','mi','fa','fa#','sol','sol#','la', 'la#', 'si', 'do','do#','re','re#','mi','fa','fa#','sol','sol#','la', 'la#', 'si','do','do#','re','re#','mi','fa','fa#','sol','sol#','la', 'la#', 'si','do','do#','re','re#','mi','fa','fa#','sol','sol#','la', 'la#', 'si','do','do#','re','re#','mi','fa','fa#','sol','sol#','la', 'la#', 'si', 'do']
d['do'] = ['do','re','mi','fa','sol','la','si']
d['do#'] = ['do#','re#','fa','fa#','sol#','la#','do']
d['re'] = ['re','mi','fa#','sol','la','si','do#']
d['re#'] = ['re#','fa','sol','sol#','la#','do','re']
d['mi'] = ['mi','fa#','sol#','la','si','do#','re#']
d['fa'] = ['fa','sol','la','la#','do','re','mi']
d['fa#'] = ['fa#','sol#','la#','si','do#','re#','fa']
d['sol'] = ['sol','la','si','do','re','mi','fa#']
d['sol#'] = ['sol#','la#','do','do#','re#','fa','sol']
d['la'] = ['la','si','do#','re','mi','fa#','sol#']
d['la#'] = ['la#','do','re','re#','fa','sol','la']
d['si'] = ['si','do#','re#','mi','fa#','sol#','la#']

entNumero = []
entNota = []
deuCerto = []

for i in range(N): #popula numeros
	entNumero.append(int(input())-1)

for i in entNumero: #converte os numeros para notas
	if(escala[i] not in entNota):
		entNota.append(escala[i]);

for i in d:
	for j in entNota:
		if j in d[i]:
			continue
		else:
			break
	else:
		deuCerto.append(i)
		
m = {}
if(len(deuCerto) == 0):
	print("desafinado")
else:
	for i in escala:
		if i in deuCerto:
			print(i)
			break