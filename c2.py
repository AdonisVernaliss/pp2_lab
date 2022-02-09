n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    arr[0][i] = i
    arr[i][0] = i
    arr[i][i] = i*i

for i in arr:
    for j in i:
        print(j,end=' ')
    print()