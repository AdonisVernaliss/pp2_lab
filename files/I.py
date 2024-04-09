n=int(input())
l=[]
for i in range(0,n):
    l.append(input())

for i in l:
    if i.find("@gmail.com") != -1:
        i=i.replace("@gmail.com","")
        print(i)