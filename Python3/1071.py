# -*- coding: utf-8 -*-

x = int(input())
y = int(input())

if x < y:
	passo = 1
	x = x+1
else:
	passo = -1
	x = x-1

soma = 0
for i in range(x, y, passo):
	#print(i)	
	if i%2 == 1: #Impar
		soma += i

print(soma)