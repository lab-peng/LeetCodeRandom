from collections import Counter
bank = ["011001", "000000", "000000", "010100", "001000"]
bank = [Counter(b) for b in bank]
print(bank)

l, r = 0, 1
ans = 0
while r < len(bank):
    while r < '1' not in bank[r]:
        r += 1
    if l != r:
        ans += bank[l].get('1') * bank[r].get('1')
    l = r
    r += 1



# for r in range(1, len(bank)):
#     while '1' not in bank[r]:
#         r += 1
#     if l != r:
#         # ans += bank[l].get('1') * bank[r].get('1')
#         print(l, r)
#     l = r
#
print(ans)

