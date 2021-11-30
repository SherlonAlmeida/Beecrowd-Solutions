# -*- coding: utf-8 -*-

notas = list(map(float, input().split()))
pesos = [2, 3, 4, 1]

media = 0.0
for i in range(4):
	media += notas[i]*(pesos[i]/10)

trunc = int(media*10)
trunc = trunc/10

print("Media: %.1f" % (trunc))

if media >= 7.0:
	print("Aluno aprovado.")

elif media < 5.0:
	print("Aluno reprovado.")

elif media >=5 and media < 7.0:
	print("Aluno em exame.")

	exame = float(input())
	print("Nota do exame: %.1f" % (exame))
	novo_calc = (media + exame)/2

	if media >= 5.0:
		print("Aluno aprovado.")
	else:
		print("Aluno reprovado.")

	print("Media final: %.1f" % (novo_calc))
