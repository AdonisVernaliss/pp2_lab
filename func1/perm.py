from itertools import permutations

st = input()
def doPer(s):
    l = []
    l[:] = st
    perm = permutations(l)
    for i in list(perm):
        print(i)
doPer(st)