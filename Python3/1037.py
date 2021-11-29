# -*- coding: utf-8 -*-

entrada = float(input())
if entrada < 0 or entrada > 100:
	print("Fora de intervalo")
elif entrada <= 25.0:
	print("Intervalo [0,25]")
elif entrada <= 50.0:
	print("Intervalo (25,50]")
elif entrada <= 75.0:
	print("Intervalo (50,75]")
else:
	print("Intervalo (75,100]")