def genDiv34(n):
    i = 0
    while (i*3*4 <= n):
        yield i*3*4
        i+=1
n=int(input())
div34 = genDiv34(n)

for i in div34:
    print(i, end=" ")
