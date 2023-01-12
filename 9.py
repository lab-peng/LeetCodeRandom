from typing import List, Optional
from collections import defaultdict, Counter, deque, OrderedDict
from itertools import zip_longest


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """
        1329. Sort the Matrix Diagonally
        https://leetcode.com/problems/sort-the-matrix-diagonally/solutions/2493662/python-c-easiest-approach-detailed-explanation-beginner-friendly-easy-understand/
        """
        # mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
        m, n = len(mat), len(mat[0])
        hm = defaultdict(list)
        for i in range(m):
            for j in range(n):
                hm[i - j].append(mat[i][j])
        for k in hm:
            hm[k].sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j] = hm[i - j].pop()
        return mat


s = Solution()
mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
print(s.diagonalSort(mat))


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """
        arr = [1,4,2,5,3]
        :param arr:
        :return:
        """
        ans = 0
        for i in range(1, len(arr) + 1, 2):
            for j in range(len(arr) - i + 1):
                # print(arr[j: j + i])
                ans += sum(arr[j: j + i])
        return ans


s = Solution()
arr = [1, 4, 2, 5, 3]
print(s.sumOddLengthSubarrays(arr))


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        """
        2120. Execution of All Suffix Instructions Staying in a Grid
        """

        # n = 3, startPos = [0, 1], s = "RRDDLU"
        # n = 2, startPos = [1, 1], s = "LURD"
        def get_steps(string):
            i, j = startPos
            steps = 0
            for c in string:
                if c == 'D':  # note: if i == n - 1 break should be put before i += 1
                    if i == n - 1:
                        break
                    i += 1
                elif c == 'L':
                    if j == 0:
                        break
                    j -= 1
                elif c == 'U':
                    if i == 0:
                        break
                    i -= 1
                elif c == 'R':
                    if j == n - 1:
                        break
                    j += 1
                steps += 1
            return steps

        ans = []
        for i in range(len(s)):
            ans.append(get_steps(s[i:]))
        return ans


solution = Solution()
n = 3
startPos = [0, 1]
s = "RRDDLU"

n = 2
startPos = [1, 1]
s = "LURD"
print(solution.executeInstructions(n, startPos, s))


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            count = Counter(bin(i)[2:])
            ans.append(count.get('1', 0))
        return ans


s = Solution()
n = 2
print(s.countBits(n))


class Solution:
    def reverseBits(self, n: int) -> int:
        """
        190. Reverse Bits
        """
        # TODO: This won't work.  It should be implemented with bit operation
        return int(str(n)[::-1], 2)


s = Solution()
n = 11111111111111111111111111111101
print(s.reverseBits(n))


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        268. Missing Number
        :param nums:
        :return:
        """
        nums.sort()
        for i, j in zip_longest(range(len(nums) + 1), nums):
            if i != j or j is None:
                return i


s = Solution()
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
nums = [0, 1]
print(s.missingNumber(nums))


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        return ans


s = Solution()
nums = [1, 2, 3, 4]
print(s.productExceptSelf(nums))


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        36. Valid Sudoku
        """
        row, col, cube = set(), set(), set()

        for r in range(len(board)):
            for c in range(len(board)):
                digit = board[r][c]

                if digit == '.':
                    continue
                if (r, digit) in row:
                    return False
                if (c, digit) in col:
                    return False
                if (r // 3, c // 3, digit) in cube:
                    return False

                row.add((r, digit))
                col.add((c, digit))
                cube.add((r // 3, c // 3, digit))
        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

s = Solution()
print(s.isValidSudoku(board))


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # grt = float('-inf')
        # ans = [-1]
        # for i in range(len(arr) - 1, 0, -1):
        #     grt = max(grt, arr[i])
        #     ans.append(grt)
        # ans.reverse()
        # return ans

        grt = float('-inf')
        d = deque([-1])
        for i in range(len(arr) - 1, 0, -1):
            grt = max(grt, arr[i])
            d.appendleft(grt)
        # print(*d)
        return d


s = Solution()
arr = [17, 18, 5, 4, 6, 1]
print(s.replaceElements(arr))


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        392. Is Subsequence
        :param s:
        :param t:
        :return:
        """
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


solution = Solution()
s = "aec"
t = "abcde"
print(solution.isSubsequence(s, t))


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = strs[0]
        for s in strs:
            if len(s) < len(shortest):
                shortest = s

        lgst = ''
        for i in range(len(shortest)):
            if len({x[i] for x in strs}) != 1:
                return lgst
            lgst += shortest[i]
        return lgst


s = Solution()
strs = ["flower", "flow", "flight"]
# strs = ["dog", "racecar", "car"]
strs = ['ab', 'a']
print(s.longestCommonPrefix(strs))


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        https://leetcode.com/problems/pascals-triangle/
        """
        # numRows = 5
        ans = [[1] * i for i in range(1, numRows + 1)]
        for i in range(2, numRows):
            for j in range(1, len(ans[i]) - 1):
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
        return ans


numRows = 5
s = Solution()
print(s.generate(numRows))


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        27. Remove Element
        """
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)


s = Solution()
nums, val = [3, 2, 2, 3], 3
# nums, val = [0, 1, 2, 2, 3, 0, 4, 2],  2
print(s.removeElement(nums, val))


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """
        929. Unique Email Addresses
        """
        hm = {}
        for e in emails:
            local_name, domain_name = e.split('@')
            local_name = local_name.replace('.', '')
            if '+' in local_name:
                local_name = local_name[:local_name.index('+')]
            processed_e = local_name + '@' + domain_name
            hm[processed_e] = hm.get(processed_e, 0) + 1
        return len(hm)


solution = Solution()
emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
print(solution.numUniqueEmails(emails))


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        205. Isomorphic Strings
        """
        hm_s, hm_t = {}, {}
        for c1, c2 in zip(s, t):
            if (c1 in hm_s and hm_s[c1] != c2) or (c2 in hm_t and hm_t[c2] != c1):
                return False
            # print(hm_s, hm_t)
            hm_s[c1] = c2
            hm_t[c2] = c1
        return True


solution = Solution()
s = "paper"
t = "title"
s = "bbbaaaba"
t = "aaabbbba"
s = 'egg'
t = 'add'
s = "badc"
t = 'baba'
print(solution.isIsomorphic(s, t))


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        605. Can Place Flowers
        """
        # TODO


flowerbed, n = [1, 0, 0, 0, 1], 2
flowerbed, n = [1, 0, 0, 0, 0, 0, 1], 2
# flowerbed, n = [0, 0, 1, 0, 1], 1
s = Solution()
print(s.canPlaceFlowers(flowerbed, n))
