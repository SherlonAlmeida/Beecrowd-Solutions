NOME = input()
SALARIO = float(input())
VENDAS = float(input())
BONUS = (15*VENDAS)/100
TOTAL = SALARIO + BONUS
print("TOTAL = R$ %.2f" % (TOTAL))