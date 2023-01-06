# 1024 Palindromic Number

def is_palin_num(num: int) -> bool:
    str_num = str(num)
    l, r = 0, len(str_num) - 1
    while l < r:
        if str_num[l] != str_num[r]:
            return False
        l += 1
        r -= 1
    return True


def get_palin_num(n: int, k: int) -> list:
    steps = 0
    current = n
    while not is_palin_num(current):
        current_reverse = int(str(current)[::-1])
        current += current_reverse
        steps += 1
        if steps == k:
            break
    return [current, steps]


def main():
    k, n = input('').split()
    ans = get_palin_num(int(k), int(n))

    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
