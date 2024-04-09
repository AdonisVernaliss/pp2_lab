es = input()

for i in es:
    if not (i.islower() or i.isupper() or i.isdigit() or i==' '):
        # if (ord(i)<=48 or ord(i)>=57) and (ord(i)<=65 or ord(i)>=90) and (ord(i)<=97 and ord(i)>=122):
        # print (1)
        es = es.replace(i,'')


l = list(es.split())

l = list(dict.fromkeys(l))
l.sort()

print(len(l))
for i in l:
    print(i)