assassinatos = dict()
mortos = set()
while True:
    try:
        assassino, assassinado = input().split()
        mortos.add(assassinado)          #Coloca o morto na lista de mortos
        try:
            assassinatos[assassino] += 1 #Incrementa espaco do assassino
        except KeyError as e:
            assassinatos[assassino] = 1 #Cria o espaco para o assassino
    except EOFError:
        break

print("HALL OF MURDERERS")
for key in sorted(assassinatos):
    if(key not in mortos):
        print(key, assassinatos[key])