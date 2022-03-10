import re

with open('row.txt', 'rb') as f:
    response = f.read().decode('utf-8')
pattern = r'[ ,.]'
l = re.sub(pattern, '|', response)# or l.replace(' ', '|').replace(',', '|').replace('.', '|')
print(l)
