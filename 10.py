from typing import List, Optional
from collections import Counter, deque

from binary_tree import TreeNode, list_to_tree


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
        return next(iter((count_t - count_s).keys()))


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """
        1302. Deepest Leaves Sum
        """
        q = deque()
        if root:
            q.append(root)

        while q:
            lvl_total = 0
            for i in range(len(q)):
                current = q.popleft()
                # print(current.val)
                lvl_total += current.val

                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        return lvl_total


root = list_to_tree([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])
# root.graph()
s = Solution()
print(s.deepestLeavesSum(root))


class Solution:
    def __init__(self):
        self.sum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        1038. Binary Search Tree to Greater Sum Tree
        """

        def dfs(root):
            if not root:
                return
            dfs(root.right)
            self.sum += root.val
            root.val = self.sum
            # print(root.val)
            dfs(root.left)

        dfs(root)
        return root


root = list_to_tree([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
# root.graph()
s = Solution()


# s.bstToGst(root)
# s.bstToGst(root).graph()


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        """
        2265. Count Nodes Equal to Average of Subtree
        """

        self.memo = {}
        self.sum = 0

        def count_sum(root):
            if root in self.memo:
                return self.memo[root]
            if not root:
                return 0, 0
            count = 1 + count_sum(root.left)[0] + count_sum(root.right)[0]
            total = root.val + count_sum(root.left)[1] + count_sum(root.right)[1]
            self.memo[root] = (count, total)
            return count, total

        count_sum(root)
        # print(self.memo)

        ans = 0
        for k, v in self.memo.items():
            if k.val == v[1] // v[0]:
                ans += 1
        return ans


root = list_to_tree([4, 8, 5, 0, 1, None, 6])
root = list_to_tree([0, 0, 0])
# root.graph()
s = Solution()
print(s.averageOfSubtree(root))


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        654. Maximum Binary Tree
        """
        if not nums:
            return
        root = TreeNode(max(nums))
        mid = nums.index(max(nums))
        left = nums[:mid]
        right = nums[mid + 1:]

        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        return root


nums = [3, 2, 1, 6, 0, 5]
s = Solution()
root = s.constructMaximumBinaryTree(nums)


# root.graph()


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        """
        1008. Construct Binary Search Tree from Preorder Traversal
        """
        if not preorder:
            return
        root = TreeNode(preorder[0])
        left = [i for i in preorder if i < preorder[0]]
        right = [i for i in preorder if i > preorder[0]]
        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)

        return root


preorder = [8, 5, 1, 7, 10, 12]
s = Solution()
root = s.bstFromPreorder(preorder)
root.graph()


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        """
        1305. All Elements in Two Binary Search Trees
        """

        def inorder(root):
            if not root:
                return []
            return [*inorder(root.left), *[root.val], *inorder(root.right)]

        inorder_root1 = inorder(root1)
        inorder_root2 = inorder(root2)

        # return sorted([*inorder_root1, *inorder_root2])

        ans = []
        l, r = 0, 0
        while l < len(inorder_root1) and r < len(inorder_root2):
            if inorder_root1[l] > inorder_root2[r]:
                ans.append(inorder_root2[r])
                r += 1
            else:
                ans.append(inorder_root1[l])
                l += 1
        return ans + inorder_root1[l:] + inorder_root2[r:]


root1 = list_to_tree([2, 1, 4])
root2 = list_to_tree([1, 0, 3])
# root1.graph()
# root2.graph()
s = Solution()
print(s.getAllElements(root1, root2))


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        """
        2331. Evaluate Boolean Binary Tree
        """
        if not root.left and not root.right:
            return bool(root.val)

        if root.val == 2:
            if root.left.val in [0, 1] and root.right.val in [0, 1]:
                return bool(root.left.val or root.right.val)
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)

        elif root.val == 3:
            if root.left.val in [0, 1] and root.right.val in [0, 1]:
                return bool(root.left.val and root.right.val)
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)


root = list_to_tree([2, 1, 3, None, None, 0, 1])
# root = list_to_tree([0])
# root.graph()
s = Solution()
print(s.evaluateTree(root))


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        617. Merge Two Binary Trees
        """
        if not root1 and not root2:
            return None
        if not root2:
            return root1
        if not root1:
            return root2
        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)

        return root


root1, root2 = list_to_tree([1, 3, 2, 5]), list_to_tree([2, 1, 3, None, 4, None, 7])
# root1, root2 = list_to_tree([1, 2, 3]), list_to_tree([1, 2, 3])
# root1.graph()
# root2.graph()

s = Solution()
root = s.mergeTrees(root1, root2)


# root.graph()

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """
        897. Increasing Order Search Tree
        """

        def inorder(root):
            if not root:
                return []
            return [*inorder(root.left), root.val, *inorder(root.right)]

        root_list = inorder(root)

        node = TreeNode(root_list[0])
        current = node  # we need a temp to save current node
        for i in range(1, len(root_list)):
            right = TreeNode(root_list[i])
            current.right = right
            current = current.right

        return node


root = list_to_tree([5, 3, 6, 2, 4, None, 8, 1, None, None, None, None, None, 7, 9])
# root.graph()

s = Solution()
ans = s.increasingBST(root)


# ans.graph()


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hs = set()
        l = 0
        min_cards = float('inf')

        for r in range(len(cards)):
            while cards[r] in hs:
                hs.remove(cards[l])
                l += 1
                min_cards = min(min_cards, r - l + 2)
            hs.add(cards[r])
        return min_cards if min_cards != float('inf') else -1


s = Solution()
cards = [3, 4, 2, 3, 4, 7]
# cards = [95, 11, 8, 65, 5, 86, 30, 27, 30, 73, 15, 91, 30, 7, 37, 26, 55, 76, 60, 43, 36, 85, 47, 96, 6]
print(s.minimumCardPickup(cards))


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        112. Path Sum
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


root, targetSum = list_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1]), 22
# root.graph()
s = Solution()
print(s.hasPathSum(root, targetSum))


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        113. Path Sum II
        """
        if not root:
            return []

        q = deque([(root, targetSum, [])])
        paths = []
        while q:
            current, target_sum, path = q.popleft()
            if not current.left and not current.right and current.val == target_sum:
                paths.append(path + [current.val])
            if current.left:
                q.append((current.left, target_sum - current.val, path + [current.val]))
            if current.right:
                q.append((current.right, target_sum - current.val, path + [current.val]))

        return paths


root, targetSum = list_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]), 22
root.graph()
s = Solution()
print(s.pathSum(root, targetSum))
