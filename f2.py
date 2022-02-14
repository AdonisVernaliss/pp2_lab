n = int(input())
d = {}
inp = []

name = ''
comp = 0

for i in range(n):
    name, comp = map(str, input().split())

    if name in d.keys():
        d[name] = d[name] + int(comp)
    else:
        d[name] = int(comp)

# print(d)

imax = max(d, key=d.get)
# print(imax)
# print(imax, d[imax])
key_list = list(d.keys())
key_list.sort()

for i in key_list:
    if d[imax] - d[i] != 0:
        print(i, 'has to receive', d[imax] - d[i], "tenge")
    else:
        print(i, 'is lucky!')
