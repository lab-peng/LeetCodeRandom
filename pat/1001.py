# 1001 A+B Format
def format_num(num: int) -> str:
    x = str(num)[::-1]
    ans = ''
    for i in range(len(x)):
        if i % 3 == 0:
            ans += ','
        ans += x[i]
    return ans[::-1].strip(',').replace('-,', '-')


def main():
    a, b = [int(x) for x in input('').split()]
    print(format_num(a + b))


if __name__ == '__main__':
    main()
