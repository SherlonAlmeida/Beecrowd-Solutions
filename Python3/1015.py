from math import *
x1,y1 = list(map(float, input().split()))
x2,y2 = list(map(float, input().split()))
distancia = sqrt((x2-x1)**2 + (y2-y1)**2)
print("%.4f" % (distancia))