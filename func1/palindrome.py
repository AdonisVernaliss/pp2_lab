n = input()
def palindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False
print(palindrome(n))