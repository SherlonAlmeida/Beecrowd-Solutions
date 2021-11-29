dias = int(input())
A = 0
M = 0
D = 0
while dias != 0:
    if dias - 365 >= 0:
        dias -= 365
        A += 1
    elif dias - 30 >= 0:
        dias -= 30
        M += 1
    else:
        dias -= 1
        D += 1
print("%d ano(s)" % (A))
print("%d mes(es)" % (M))
print("%d dia(s)" % (D))