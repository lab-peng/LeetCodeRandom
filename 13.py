# from collections import Counter
# bank = ["011001", "000000", "000000", "010100", "001000"]
# bank = [Counter(b) for b in bank]
# print(bank)
#
# l, r = 0, 1
# ans = 0
# while r < len(bank):
#     while r < '1' not in bank[r]:
#         r += 1
#     if l != r:
#         ans += bank[l].get('1') * bank[r].get('1')
#     l = r
#     r += 1
#
#
#
# # for r in range(1, len(bank)):
# #     while '1' not in bank[r]:
# #         r += 1
# #     if l != r:
# #         # ans += bank[l].get('1') * bank[r].get('1')
# #         print(l, r)
# #     l = r
# #
# print(ans)

class Solution:
    def maxDepth(self, s: str) -> int:
        """
        1614. Maximum Nesting Depth of the Parentheses
        """
        hm = {
            ')': '('
        }
        stack = []
        max_depth = float('-inf')

        for c in s:
            if c not in '()':
                continue
            if c not in hm:
                stack.append(c)
                continue
            # if not stack or stack[-1] != hm[c]:
            #     return False
            # print(stack)
            max_depth = max(max_depth, len(stack))
            stack.pop()

        return max_depth



s = "(1+(2*3)+((8)/4))+1"
solution = Solution()
print(solution.maxDepth(s))
