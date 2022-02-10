up=0
lo=0
nu=0
pa_list = []
n = int(input())

for i in range(n):
    pa = input()
    pa_list.append(pa)
    
#print(dict.fromkeys(pa_list))
pa_list = list(dict.fromkeys(pa_list))
pa2_list = []
c=0
for i in pa_list:
    for j in i:
        if j.isdigit():
            # print(0)
            nu+=1
        elif j.islower():
            # print(1)
            lo+=1
        elif j.isupper():
            # print(2)
            up+=1

    if (nu > 0) and (lo > 0) and (up > 0):
        pa2_list.append(i)

    lo=0
    nu=0
    up=0
print(len(pa2_list))
pa2_list.sort()
for i in pa2_list:
    print(i)