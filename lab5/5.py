import re

with open('row.txt', 'rb') as f:
    response = f.read().decode('utf-8')
pattern = r'а.*?б\b|a.*?b\b'
l = re.findall(pattern, response)
print(l)
