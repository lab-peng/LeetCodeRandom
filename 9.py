from typing import List, Optional
from collections import defaultdict


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
