h = int(input())
l = int(input())

def solve(h,l):
    r= (l-h*2)//2
    c = h-r
    print(c , r)

solve(h,l)