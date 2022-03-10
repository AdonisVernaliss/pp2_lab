import re

with open('row.txt', 'rb') as f:
    response = f.read().decode('utf-8')
pattern = r'[A-Z]|[А-Я]'
l = re.split(pattern, response)
print(*l)
