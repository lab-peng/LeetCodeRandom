# 1015 Reversible Primes
def to_n_base(num: int, radix: int) -> str:  # 1 < n <= 10
    ans = ""
    while num != 0:
        ans = str(num % radix) + ans
        num = num // radix
    return ans


def to_decimal(n_base: str, n: int) -> int:
    return int(n_base, n)


def is_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


nums = input('').split()
while nums[0] != '-2':
    a, b = int(nums[0]), int(nums[1])
    n_base = to_n_base(a, b)
    n_base_reverse = n_base[::-1]
    decimal_num = to_decimal(n_base_reverse, b)
    if is_prime(a) and is_prime(decimal_num):
        print('Yes')
    else:
        print("No")
    nums = input('').split()

a = input().split()
while a[0][0] != '-':
    if is_prime(int(a[0])) and is_prime(int(to_n_base(int(a[0]), int(a[1]))[::-1],int(a[1]))):
        print("Yes")
    else:
        print("No")
    a = input().split()



# print(to_n_base(23, 2))
# print(to_decimal('10111', 2))
# print(to_decimal('11101', 2))
# print(is_prime(73))


