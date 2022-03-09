import re

with open('row.txt', 'rb') as f:
    response = f.read().decode('utf-8')
l = re.sub(r'(\w| )([A-Z])', r'\1 \2', response)
print(l)
