n =int(input())

a = input()

if a == 'k':
    c = int(input())
    f = float(n/1024)
    f=round(f,c)
    print(f)
elif a == 'b':
    print(n * 1024)
