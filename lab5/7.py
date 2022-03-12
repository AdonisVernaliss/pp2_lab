def snake_to_camel(snc):
    return ''.join(x.capitalize() or '_' for x in snc.split('_'))


l = input()
print(snake_to_camel(l))

#import camelcase
#c = camelcase.CamelCase()
#txt = input()
#print(c.hump(txt))
