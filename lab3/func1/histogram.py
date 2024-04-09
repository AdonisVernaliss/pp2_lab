l=list(map(int, input().split()))

def histogram(l):
    for i in l:
        for j in range(i):
            print("*", end="")
        print()
histogram(l)