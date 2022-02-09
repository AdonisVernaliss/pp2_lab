n = int(input())
insh = []
outsh = []
for i in range(n):
    l = list(map(str, input().split()))
    if l[0] == '1':
        insh.append(l[1])
    else:
        s = insh[0]
        outsh.append(s)
        insh.pop(0)
for i in outsh:
    print(i, end=" ")
