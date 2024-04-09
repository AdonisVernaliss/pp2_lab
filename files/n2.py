n = int(input())
l = []

while n != 0:
    l.append(n)
    n = int(input())

for i in range(int(len(l) / 2)):
    print(l[i] + l[-i - 1], end=' ')

if len(l) % 2 == 1:
    print(l[int(len(l) / 2)])
