import re
with open('row.txt', 'rb') as f:
    response = f.read().decode('utf-8')
pattern = r'[A-Z][a-z]+|[А-Я][а-я]+'
l = re.findall(pattern, response)
print(l)