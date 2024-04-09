from math import sqrt

x1, y1 = map(int, input().split())

n = int(input())
coord_list = []
dis_list = []

for i in range(n):
    x2, y2 = map(int, input().split())
    d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    coord_list.append([x2, y2])
    dis_list.append(d)

r = [x for i, x in sorted(zip(dis_list, coord_list))]

for i in r:
    print(*i)
