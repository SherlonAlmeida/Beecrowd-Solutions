seg = int(input())
H = 0
M = 0
S = 0
while seg != 0:
    if seg - 3600 >= 0:
        seg -= 3600
        H += 1
    elif seg - 60 >= 0:
        seg -= 60
        M += 1
    else:
        seg -= 1
        S += 1
print("%d:%d:%d" % (H,M,S))