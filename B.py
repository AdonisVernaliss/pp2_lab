s = input()
b = 0
for i in s:
    a = ord(i)
    b += a
if b > 300:
    print("It is tasty!")
else:
    print("Oh, no!")