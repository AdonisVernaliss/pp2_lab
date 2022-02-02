b=input()
a=[]
for i in range(0,len(b)):
    a.insert(0,b[i])
p=1
r=0
for i in a:
    if i == '1':
        r+=p
    p*=2

print(r)