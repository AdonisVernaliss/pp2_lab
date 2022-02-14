br = input()

lb = []

for i in range(len(br)):
    if br[i] == '{' or br[i] == '(' or br[i] == '[':
        lb.append(br[i])

    elif br[i] == '}' and len(lb) > 0 and lb[-1] == '{':
        lb.pop(-1)

    elif br[i] == ')' and len(lb) > 0 and lb[-1] == '(':
        lb.pop(-1)

    elif br[i] == ']' and len(lb) > 0 and lb[-1] == '[':
        lb.pop(-1)

    else:
        lb.append('/')
        break
# {(})
# {(} ////

if len(lb) == 0:
    print("Yes")
else:
    print("No")
