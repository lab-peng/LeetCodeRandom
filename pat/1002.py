# 1002 A+B for Polynomials
from collections import Counter

# p1 = [float(x) for x in input('').split()]
# p2 = [float(x) for x in input('').split()]
p1 = [2, 1, 2.4, 0, 3.2]
p2 = [2, 2, 1.5, 1, 0.5]


def get_pol_hm(p):
    hm = {}
    for i in range(1, len(p), 2):
        hm[p[i]] = p[i + 1]
    return hm


pol1 = get_pol_hm(p1)
pol2 = get_pol_hm(p2)


count = Counter(pol1) + Counter(pol2)
ans = [str(len(count)),]
for key in sorted(count, reverse=True):
    ans.append(str(int(key)))
    coeffi = round(count[key], 1)
    ans.append(str(coeffi))

# print(' '.join(ans))
print(*ans)