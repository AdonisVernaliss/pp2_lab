isPrime = lambda a,b: a%b
l = list(map(int, input().split()))

def filter(l):
    i=0
    while(i!=len(l)):
        if l[i] == 1:
            pass
        elif l[i] > 1:
            for j in range(2,l[i]):
                if isPrime(l[i],j)==0:
                    l.pop(i)
                    i-=1
                    break
        else:
            l.pop(i)
        i+=1
filter(l)
print(l)

