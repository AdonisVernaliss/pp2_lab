import re

pattern = r'\S*[a-z]+_[a-z]+\S*|\S*[а-я]_[а-я]\S*'
with open('row.txt', 'rb') as f:
    response = f.read().decode('utf-8')
l = re.findall(pattern, response)
print(l)
