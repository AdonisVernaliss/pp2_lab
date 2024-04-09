l = list(map(int, input().split()))
c = 0


def three(nums):
    global c
    for i in range(len(l) - 2):
        if (l[i] == 3) and (l[i + 1] == 3):
            c = 1
    if c == 1:
        return True
    else:
        return False


ans = three(l)
print(ans)
