from typing import List, Optional
from collections import Counter


class Solution:
    def minPartitions(self, n: str) -> int:
        """
        1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
        """
        return max([int(digit) for digit in n])


s = Solution()
n = "32"
print(s.minPartitions(n))


class SubrectangleQueries:
    """
    1476. Subrectangle Queries
    """

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]

    def getRectangle(self):
        return self.rectangle


r = [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]
obj = SubrectangleQueries(r)
r1, c1, r2, c2, new_val = 0, 0, 3, 2, 5
obj.updateSubrectangle(r1, c1, r2, c2, new_val)
param_2 = obj.getValue(1, 2)
print(param_2)
print(obj.getRectangle())


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """
        1302. Deepest Leaves Sum
        """


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)
root.right.right.right = TreeNode(8)

s = Solution()
print(s.deepestLeavesSum(root))


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = 0
        lgst = 1

        for r in range(1, len(nums)):
            if nums[r] <= nums[r - 1]:
                l = r
            lgst = max(lgst, r - l + 1)
        return lgst


s = Solution()
nums = [1, 3, 5, 4, 7]
print(s.findLengthOfLCIS(nums))


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        389. Find the Difference
        """
        count_s = Counter(s)
        count_t = Counter(t)
        # print(next(iter((count_t - count_s).keys())))
        return next(iter((count_t - count_s).keys()))
