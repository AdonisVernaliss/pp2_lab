def genSqr(a, b):
    i = 0
    for i in range(a, b + 1):
        yield (i) ** 2


a = int(input())
b = int(input())
sq = genSqr(a, b)

for i in sq:
    print(i, end=" ")
