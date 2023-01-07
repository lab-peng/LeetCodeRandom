# 1019 General Palindromic Number

def to_n_base(num: int, radix: int) -> list:
    ans = []
    while num != 0:
        ans.append(str(num % radix))
        num = num // radix
    ans.reverse()
    return ans


def is_palindrome(num: list) -> str:
    l, r = 0, len(num) - 1
    while l < r:
        if num[l] != num[r]:
            return 'No'
        l += 1
        r -= 1
    return 'Yes'


num, radix = [int(x) for x in input('').split()]
n_base = to_n_base(num, radix)
if_palindrome = is_palindrome(n_base)
print(if_palindrome)
print(' '.join(n_base))

# print(to_n_base(27, 2))
# print(to_n_base(121, 5))
#
# print(is_palindrome(to_n_base(27, 2)))
# print(is_palindrome(to_n_base(121, 5)))
