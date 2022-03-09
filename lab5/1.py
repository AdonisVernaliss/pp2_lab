import re

with open('row.txt', 'rb') as f:
    response = f.read().decode('utf-8')
pattern = r'аб{0,}|ab{0,}'
l = re.findall(pattern, response)
print(l)
