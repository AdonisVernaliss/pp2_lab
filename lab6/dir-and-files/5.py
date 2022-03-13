list = list(map(str, input().split()))
with open('anytxtfile.txt', 'w') as f:
    for i in list:
        f.write(i)
        f.write(' ')
with open('anytxtfile.txt') as f:
    response = f.read()
print(response)
