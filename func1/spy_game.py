# def spy_game(nums):
#    pass

# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False
l = list(map(int, input().split()))


def spy_game(nums):
    s = [0, 0, 7]
    c = 0
    for i in nums:
        if c == 3:
            return True
        elif i == s[c]:
            c += 1
    if c == 3:
        return True
    else:
        return False


print(spy_game(l))
