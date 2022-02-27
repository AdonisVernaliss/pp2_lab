def genEv(n):
    even = [i * 2 for i in range(int(n / 2) + 1)]
    return even


n = int(input())
even = genEv(n)
s = ''
for i in even:
    s += str(i) + ','

s = s[0:len(s) - 1]
print(s)
