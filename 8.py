from typing import List, Optional


class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.stream = [None] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        ans = []
        if None not in self.stream[:idKey]:
            for s in self.stream:
                if s is None:
                    break
                ans.append(s)
            return ans[idKey - 1:]
        return ans


obj = OrderedStream(5)
print(obj.insert(3, 'ccccc'))
print(obj.insert(1, "aaaaa"))
print(obj.insert(2, "bbbbb"))
print(obj.insert(5, "eeeee"))
print(obj.insert(4, "ddddd"))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        """
        1720. Decode XORed Array
        Note: 1 ^ == Python xor operator
              2 xor inverse is still xor
        """
        ans = [first]
        for n in encoded:
            first ^= n
            ans.append(first)
        return ans

    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        """
        1389. Create Target Array in the Given Order
        """
        # nums, index = [0, 1, 2, 3, 4], [0, 1, 2, 2, 1]
        ans = []
        for n, i in zip(nums, index):
            ans.insert(i, n)
        return ans

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        938. Range Sum of BST
        :param root:
        :param low:
        :param high:
        :return:
        """
        range_sum = []

        def in_order(root):
            if not root:
                return None
            in_order(root.left)
            if low <= root.val <= high:
                range_sum.append(root.val)
            in_order(root.right)
            return range_sum

        return sum(in_order(root))

    def decompressRLElist(self, nums: List[int]) -> List[int]:
        """
        1313. Decompress Run-Length Encoded List
        :param nums:
        :return:
        """
        ans = []
        for i in range(0, len(nums), 2):
            for j in range(nums[i]):
                ans.append(nums[i + 1])
        return ans

    def findArray(self, pref: List[int]) -> List[int]:
        """
        2433. Find The Original Array of Prefix Xor
        :param pref:
        :return:
        """
        # Input: pref = [5, 2, 0, 3, 1]
        # Output: [5, 7, 2, 3, 2]
        ans = pref[: 1]
        for i in range(1, len(pref)):
            ans.append(pref[i] ^ pref[i - 1])
        return ans

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """
        1315. Sum of Nodes with Even-Valued Grandparent
        """

        def get_grandchildren_total(root):
            total = 0
            if not root:
                return 0
            if root.left:
                if root.left.left:
                    total += root.left.left.val
                if root.left.right:
                    total += root.left.right.val
            if root.right:
                if root.right.left:
                    total += root.right.left.val
                if root.right.right:
                    total += root.right.right.val
            return total

        res = []

        def pre_order(root):
            if not root:
                return None
            if root.val % 2 == 0:
                res.append(get_grandchildren_total(root))
            pre_order(root.left)
            pre_order(root.right)
            return res

        return sum(pre_order(root))

    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        1038. Binary Search Tree to Greater Sum Tree
        :param root:
        :return:
        """
        # TODO

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        """
        Count Nodes Equal to Average of Subtree
        :param root:
        :return:
        """

        # TODO why hasn't it work?
        def get_total_subtree(root):
            if not root:
                return 0
            return get_total_subtree(root.left) + root.val + get_total_subtree(root.right)

        def node_count(root):
            if not root:
                return 0
            return node_count(root.left) + 1 + node_count(root.right)

        ans = 0
        stack = [root]
        while stack:
            current = stack.pop()
            # print(current.val, get_total_subtree(current), node_count(current))
            if current.val <= get_total_subtree(current) // node_count(current):
                ans += 1
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return ans

    def restoreString(self, s: str, indices: List[int]) -> str:
        """
        1528. Shuffle String
        :param s:
        :param indices:
        :return:
        """
        # s = "codeleet", indices = [4, 5, 6, 7, 0, 2, 1, 3]
        ans = [0] * len(s)
        for i in range(len(s)):
            ans[indices[i]] = s[i]

        return ''.join(ans)

    def cellsInRange(self, s: str) -> List[str]:
        """
        2194. Cells in a Range on an Excel Sheet
        """

        start_letter = s.split(':')[0][0]
        end_letter = s.split(':')[1][0]
        start_num = int(s.split(':')[0][1])
        end_num = int(s.split(':')[1][1])

        ans = []
        for i in range(ord(start_letter), ord(end_letter) + 1):
            for j in range(start_num, end_num + 1):
                ans.append(f'{chr(i)}{j}')
        return ans

    def numberOfSteps(self, num: int) -> int:
        """
        1342. Number of Steps to Reduce a Number to Zero
        :param num:
        :return:
        """
        ans = 0
        while num:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            ans += 1

        return ans

    def balancedStringSplit(self, s: str) -> int:
        """
        1221. Split a String in Balanced Strings
        :param s:
        :return:
        """
        # s = "RLRRLLRLRL"
        hm = {}
        ans = 0
        for i in range(len(s)):
            hm[s[i]] = hm.get(s[i], 0) + 1
            if hm.get('R') == hm.get('L'):
                ans += 1
        return ans

    def xorOperation(self, n: int, start: int) -> int:
        """
        1486. XOR Operation in an Array
        """
        ans = 0
        for i in range(start, start + n * 2, 2):
            ans ^= i

        return ans

    def sortSentence(self, s: str) -> str:
        """
        1859. Sorting the Sentence
        """
        s = s.split(' ')
        ans = [None] * len(s)
        for word_index in s:
            word = word_index[:-1]
            index = int(word_index[-1])
            ans[index - 1] = word
        return ' '.join(ans)

    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        """
        1773. Count Items Matching a Rule
        :param items:
        :param ruleKey:
        :param ruleValue:
        :return:
        """
        ans = 0
        hm = {
            'type': 0,
            'color': 1,
            'name': 2
        }

        for item in items:
            if ruleValue == item[hm[ruleKey]]:
                ans += 1
        return ans

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        """
        2373. Largest Local Values in a Matrix
        """
        # Input: grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
        # Output: [[9, 9], [8, 6]]
        ans = [[0] * (len(grid) - 2) for i in range(len(grid) - 2)]
        for i in range(len(grid) - 2):
            for j in range(len(grid) - 2):
                # sub_grid = [row[j:j+3] for row in [grid[i] for i in range(i, i + 3)]]
                max_val = max([max(row[j:j + 3]) for row in [grid[i] for i in range(i, i + 3)]])
                print(max_val)
                ans[i][j] = max_val
        return ans

    def findCenter(self, edges: List[List[int]]) -> int:
        """
        1791. Find Center of Star Graph
        :param edges:
        :return:
        """
        hm = {}
        for e in edges:
            hm[e[0]] = hm.get(e[0], 0) + 1
            hm[e[1]] = hm.get(e[1], 0) + 1
        for k, v in hm.items():
            if v == len(edges):
                return k


solution = Solution()
encoded, first = [1, 2, 3], 1
print(solution.decode(encoded, first))

nums, index = [0, 1, 2, 3, 4], [0, 1, 2, 2, 1]
print(solution.createTargetArray(nums, index))

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)
low, high = 7, 15

print(solution.rangeSumBST(root, low, high))

nums = [1, 1, 2, 3]
print(solution.decompressRLElist(nums))

pref = [5, 2, 0, 3, 1]
print(solution.findArray(pref))

root = TreeNode(6)

root.left = TreeNode(7)
root.right = TreeNode(8)

root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)

root.left.left.left = TreeNode(9)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)

print(solution.sumEvenGrandparent(root))

print(solution.bstToGst(root))

# root = TreeNode(4)
# root.left = TreeNode(8)
# root.right = TreeNode(5)
# root.left.left = TreeNode(0)
# root.left.right = TreeNode(1)
# root.right.right = TreeNode(6)

root = TreeNode(1)
root.right = TreeNode(3)
root.right.right = TreeNode(1)
root.right.right.right = TreeNode(3)

print(solution.averageOfSubtree(root))

s, indices = "codeleet", [4, 5, 6, 7, 0, 2, 1, 3]
print(solution.restoreString(s, indices))

s = "K1:L2"
s = 'A1:F1'
print(solution.cellsInRange(s))

s = "RLRRLLRLRL"
s = "RLRRRLLRLL"
s = "LLLLRRRR"
print(solution.balancedStringSplit(s))

s = "is2 sentence4 This1 a3"
print(solution.sortSentence(s))

items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
ruleKey = "color"
ruleValue = "silver"
print(solution.countMatches(items, ruleKey, ruleValue))

grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
print(solution.largestLocal(grid))

edges = [[1, 2], [5, 1], [1, 3], [1, 4]]
edges = [[1, 2], [2, 3], [4, 2]]
print(solution.findCenter(edges))
