from typing import List, Optional
from collections import defaultdict, Counter, deque
from itertools import zip_longest
from binary_tree import TreeNode, list_to_tree


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
        Add 0 in the start and 0 in the end, two pointers
        """
        fs = [0] + flowerbed + [0]
        l, r = 0, 2
        ans = 0
        while r < len(fs):
            if 1 not in fs[l: r + 1]:
                l += 1
                r += 1
                ans += 1
            l += 1
            r += 1
        return ans, n <= ans


flowerbed, n = [1, 0, 0, 0, 1], 2
# flowerbed, n = [1, 0, 0, 0, 0, 0, 1], 2
# flowerbed, n = [0, 0, 1, 0, 1], 1
s = Solution()
print(s.canPlaceFlowers(flowerbed, n))


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        496. Next Greater Element I
        """
        # ans = []
        # for n1 in nums1:
        #     sub_nums2 = nums2[nums2.index(n1) + 1:]
        #     if not sub_nums2 or max(sub_nums2) < n1:
        #         ans.append(-1)
        #     else:
        #         for s in sub_nums2:
        #             if s > n1:
        #                 ans.append(s)
        #                 break
        # return ans

        # if not nums2:
        #     return None
        #
        # mapping = {}
        # result = []
        # stack = [nums2[0]]
        #
        # for i in range(1, len(nums2)):
        #     print(stack, mapping)
        #     while stack and nums2[i] > stack[-1]:  # if stack is not empty, then compare it's last element with nums2[i]
        #         mapping[stack[-1]] = nums2[
        #             i]  # if the new element is greater than stack's top element, then add this to dictionary
        #         stack.pop()  # since we found a pair for the top element, remove it.
        #     stack.append(
        #         nums2[i])  # add the element nums2[i] to the stack because we need to find a number greater than this
        #
        # for element in stack:  # if there are elements in the stack for which we didn't find a greater number, map them to -1
        #     mapping[element] = -1
        #
        # for n1 in nums1:
        #     result.append(mapping[n1])
        #
        # return result

        # TODO  logic not fully grasped or not deeply-internalized enough
        hm = {}
        ans = []
        stack = [nums2[0]]

        for i in range(1, len(nums2)):
            # print(stack, hm)
            while stack and nums2[i] > stack[-1]:
                hm[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])

        for item in stack:
            hm[item] = -1

        for n1 in nums1:
            ans.append(hm[n1])
        return ans


nums1, nums2 = [4, 1, 2], [1, 3, 4, 2]
nums1, nums2 = [2, 4], [1, 2, 3, 4]
nums1, nums2 = [1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]
nums1, nums2 = [1, 3, 5, 2, 4], [5, 4, 3, 2, 1]
s = Solution()
print(s.nextGreaterElement(nums1, nums2))


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        724. Find Pivot Index
        """
        total = sum(nums)  # O(n)

        left_sum = 0
        for i in range(len(nums)):
            right_sum = total - nums[i] - left_sum
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1


nums = [1, 7, 3, 6, 5, 6]
# nums = [6, 5, 6, 3, 7, 1]
# nums = [1, 2, 3]
# nums = [2, 1, -1]
nums = [7, 2, 3, 4, -16, 3]

s = Solution()
print(s.pivotIndex(nums))


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        94. Binary Tree Inorder Traversal
        """
        stack, ans = [], []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            node = stack.pop()
            ans.append(node.val)
            current = node.right
        return ans

        # if not root:
        #     return []
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        ans = []
        while stack:
            current = stack.pop()
            if current:
                ans.append(current.val)
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)
        return ans

        # if not root:
        #     return []
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes, ans = deque([root]), deque()
        while nodes:
            current = nodes.popleft()
            if current:
                ans.appendleft(current.val)
                nodes.appendleft(current.left)
                nodes.appendleft(current.right)
        return ans

        # if not root:
        #     return []
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def levelorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = deque()
        if root:
            q.append(root)

        while q:
            current = q.popleft()
            ans.append(current.val)

            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        return (ans)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        ans = []

        if root:
            q.append(root)

        while q:
            lvl = []
            for i in range(len(q)):
                node = q.popleft()
                lvl.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(lvl)
        return ans

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = deque()
        q = deque()

        if root:
            q.append(root)

        while q:
            lvl = []
            for i in range(len(q)):
                node = q.popleft()
                lvl.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.appendleft(lvl)
        return ans





node_list = [1, 2, None, 4, 5]
node_list = [1, 2, 3, 4, 5, 6, None, None, 9, None, 11, 12]
# node_list = [1, None, 2, None, None, 3]
node_list = [1, 2, 3, None, 5, None, 4]
root = list_to_tree(node_list)
root.graph()

s = Solution()
print(s.inorderTraversal(root))
print(s.preorderTraversal(root))
print(s.postorderTraversal(root))
print(s.levelorderTraversal(root))
print(s.levelOrder(root))
print(s.levelOrderBottom(root))
