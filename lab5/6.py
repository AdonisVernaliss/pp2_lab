with open('row.txt', 'rb') as f:
    response = f.read().decode('utf-8')
response = response.replace(' ', '|').replace(',', '|').replace('.', '|')
print(response)
