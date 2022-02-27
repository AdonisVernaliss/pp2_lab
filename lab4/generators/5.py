def downTo0(n):
    down = [n - i for i in range(n + 1)]
    return down


n = int(input())
print(*downTo0(n))
