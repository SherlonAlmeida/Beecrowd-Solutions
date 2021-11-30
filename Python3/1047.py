# -*- coding: utf-8 -*-

hi, mi, hf, mf = list(map(float, input().split()))

inicio = hi*60 + mi
fim    = hf*60 + mf

tempo = fim - inicio

if tempo <= 0.0:
	horas   = 24 + int(tempo // 60)
	minutos = int(tempo % 60)
else:
	horas   = int(tempo // 60)
	minutos = int(tempo % 60)

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (horas, minutos))
