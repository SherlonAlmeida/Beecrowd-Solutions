while True: #Enquanto
    X,Y = map(int, input().split())
    
    #Primeiro quadrante (+, +)
    if (X > 0) and (Y > 0):
        print("primeiro")

    #Segundo quadrante (-, +)
    if (X < 0) and (Y > 0):
        print("segundo")
        
    #Terceiro quadrante (-, -)
    if (X < 0) and (Y < 0):
        print("terceiro")

    #Quarto quadrante (+, -)
    if (X > 0) and (Y < 0):
        print("quarto")

    if (X == 0) or (Y == 0):
        break

