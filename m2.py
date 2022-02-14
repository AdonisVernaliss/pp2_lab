n = input()
l = []

while n != '0':
    l.append(list(n.split()))
    n = input()

for i in l:
    i[0],i[2] = i[2],i[0]

l.sort()

for i in l:
    i[0],i[2] = i[2],i[0]

for i in l:
    print(*i)