# 1027 Colors in Mars

hm = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C'}


def decimal_to_13_base(num):
    a, b = divmod(num, 13)
    return hm[a] + hm[b]


def main():
    a, b, c = [int(x) for x in input('').split()]
    print(f'#{decimal_to_13_base(a)}{decimal_to_13_base(b)}{decimal_to_13_base(c)}')


if __name__ == '__main__':
    main()
