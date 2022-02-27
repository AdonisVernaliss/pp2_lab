import math as m
n = int(input())
s = int(input())
a = s/2*m.tan(m.pi/n)
area = round(n*s*a/2)
print(area)
