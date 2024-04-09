n = int(input())
arr = [['.' for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(i+1):
        if n%2==0:
            arr[i][j]='#'
        else:
            arr[i][n-1-j]='#'

for i in arr:
    for j in i:
        print(j,end='')
    print()