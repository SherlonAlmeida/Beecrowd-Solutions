codigo, quantidade = map(int, input().split())
precos = {1: 4.0, 2: 4.5, 3: 5.0, 4: 2.0, 5: 1.5}
print("Total: R$ %.2f" % (precos[codigo]*quantidade))