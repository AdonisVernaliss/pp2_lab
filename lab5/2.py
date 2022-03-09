import re

with open('row.txt', 'rb') as f:
    response = f.read().decode('utf-8')
pattern = r'аб{2,3}|ab{2,3}'
l = re.findall(pattern, response)
print(l)
