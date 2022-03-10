import re

with open('row.txt', 'rb') as f:
    response = f.read().decode('utf-8')
pattern = r'\S*аб{2,3}\S*|\S*ab{2,3}\S*'
l = re.findall(pattern, response)
print(l)
