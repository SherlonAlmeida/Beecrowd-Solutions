# -*- coding: utf-8 -*-

prod = list(map(int, input().split()))
preco = {1: 4.0, 2: 4.5, 3: 5.0, 4: 2.0, 5: 1.5}

a = preco[prod[0]] #Codigo
b = prod[1] #Quantidade
print("Total: R$ %.2f" % (a*b))