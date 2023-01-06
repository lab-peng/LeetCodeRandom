# 1010 Radix
# TODO: why 'Partially Accepted'?
from collections import defaultdict

def make_hm():
    hm = defaultdict(str)
    for i in range(10):
        hm[i] = str(i)
    for c in 'abcdefghijklmnopqrstuvwxyz':
        hm[ord(c) - 87] = c
    return hm


def make_hm_reverse():
    hm = make_hm()
    return {v: k for k, v in hm.items()}


def to_n_base(decimal_number: int, n: int) -> str:
    hm = make_hm()
    stack = []
    while decimal_number > 0:
        remainder = decimal_number % n
        stack.append(hm[remainder])
        decimal_number //= n
    return ''.join([x for x in reversed(stack)])


def to_decimal(n_base: str, n: int):
    hm_reverse = make_hm_reverse()
    decimal_num = 0
    for i in range(1, len(n_base) + 1):
        decimal_num += hm_reverse[n_base[-i]] * (n ** (i - 1))
    return decimal_num


# print(to_n_base(42, 2))  # => '101010'
# print(to_decimal('110', 2))  # => 14

def main():
    a, b, c, d = '6', '110', 1, 10
    a, b, c, d = '1', 'ab', 1, 2
    # a, b, c, d = input('').split()
    if c == '1':
        decimal_num = to_decimal(a, int(d))
    else:
        decimal_num = to_decimal(b, int(d))

    for i in range(2, 36):
        if to_n_base(decimal_num, i) == b:
            return i
    return 'Impossible'

if __name__ == '__main__':
    print(main())
