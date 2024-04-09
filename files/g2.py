n = int(input())

demon_list=[]

for i in range(n):
    d,w=map(str,input().split())

    demon_list.append(w)

m = int(input())

for i in range(m):
    h,a,k = map(str, input().split())

    for j in range(int(k)):
        if a in demon_list:
            ind = demon_list.index(a)
            demon_list.pop(ind)
            
print("Demons left:",len(demon_list))