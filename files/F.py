n = int(input())
a = []
for i in range(0,n):
    a.append(int(input()))



for i in a:
    if i <= 10:
        print("Go to work!")
    if 10 < i <= 25:
        print("You are weak")
    if 25 < i <= 45:
        print("Okay, fine")
    if i > 45:
        print("Burn! Burn! Burn Young!")