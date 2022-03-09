import re

with open('row.txt', 'rb') as f:
    response = f.read().decode('utf-8')
pattern = r'[A-Z][^A-Z]*'
l = re.findall(pattern, response)
print(l)
