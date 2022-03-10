import re

with open('row.txt', 'rb') as f:
    response = f.read().decode('utf-8')
l = re.sub(r'([A-Z][a-z]*)([A-Z][a-z]*)([А-Я][а-я]*)([А-Я][а-я]*)', r'\1 \2', 'CafeAnans')

print(l)
