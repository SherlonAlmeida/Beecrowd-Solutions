N = int(input())
dentro = 0

for i in range(N):
    x = int(input())
    if x >= 10 and x <= 20:
        dentro += 1

print(dentro, "in")
print(N-dentro, "out")