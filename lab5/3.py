import re

pattern = r'[a-z]_[a-z]|[а-я]_[а-я]'
with open('row.txt', 'rb') as f:
    response = f.read().decode('utf-8')
l = re.findall(pattern, response)
print(l)
