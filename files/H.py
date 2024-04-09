s=input()
k=input()
e=s.count(k)
if e > 1:
    print(s.index(k), s.rindex(k))
if e == 1:
    print(s.index(k))
