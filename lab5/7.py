def snake_to_camel(snake_case):
    return ''.join(x.capitalize() or '_' for x in snake_case.split('_'))


l = input()

print(snake_to_camel(l))
