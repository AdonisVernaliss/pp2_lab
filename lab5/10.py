import re


def snake_case(s):
    return '_'.join(re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', s.replace('-', ' '))).split()).lower()


s = input()
print(snake_case(s))
