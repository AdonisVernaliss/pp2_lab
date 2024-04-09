num = list(map(int, input().split()))
num2 = 0
if (len(num) == 1):
    num2 = int(input())
arr = []

if len(num) == 2:
    for i in range(num[0]):
        arr.append(num[-1] + 2 * i)
else:
    for i in range(num[0]):
        arr.append(num2 + 2 * i)

r = 0
for i in arr:
    r = r ^ i

print(r)
