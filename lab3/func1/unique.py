l = list(input().split())

def Unique(l):
    l = list(dict.fromkeys(l))
    return l
print(Unique(l))