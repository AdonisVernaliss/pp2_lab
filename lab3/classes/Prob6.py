isPrime = lambda a,b: a%b
l = [15,13,-19,29,654,65]

def filter(l):
    i=0
    while(i!=len(l)):
        # print(l[i],end=' ')
        if i > 1:
            for j in range(2,l[i]):
                if isPrime(l[i],j)==0:      # if not(isPrime(l[i],j))
                    l.pop(i)
                    i-=1
                    break
                    
        else:
            l.pop(i)
        i+=1

# 13 11

filter(l)
print(l)

