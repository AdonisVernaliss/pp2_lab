str = input()
a = b = 0
for i in str:
    if i.isupper():
        a += 1
    elif i.islower():
        b += 1
print(a, b)
