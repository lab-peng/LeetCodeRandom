# 1100 Mars Numbers
def make_hm(num_string: str) -> dict:
    hm = {}
    num_list = num_string.split(', ')
    for i in range(1, 13):
        hm[i] = num_list[i - 1]
    return hm

str1 = "jan, feb, mar, apr, may, jun, jly, aug, sep, oct, nov, dec"
str2 = "tam, hel, maa, huh, tou, kes, hei, elo, syy, lok, mer, jou"
hm1 = {0: 'tret'}
hm1.update(make_hm(str1))
hm1_reverse = {v: k for k, v in hm1.items()}

hm2 = make_hm(str2)
hm2_reverse = {v: k for k, v in hm2.items()}


def earth_to_mars(num: int) -> str:
    num2, num1 = divmod(num, 13)
    return f'{hm2[num2]} {hm1[num1]}' if num2 else str(hm1[num1])


def mars_to_earth(num: str) -> str:
    num = num.split(' ')
    if len(num) == 2:
        return hm2_reverse[num[0]] * 13 + hm1_reverse[num[1]]
    else:
        return hm2_reverse[num[0]] * 13 if num[0] in hm2_reverse else hm1_reverse[num[0]]


def main():
    count = input('')
    nums = []
    for i in range(int(count)):
        nums.append(input(''))

    for num in nums:
        if num.isdigit():
            print(earth_to_mars(int(num)))
        else:
            print(mars_to_earth(num))

if __name__ == '__main__':
    main()

# print(mars_to_earth('elo nov'))
# print(mars_to_earth('tam'))
