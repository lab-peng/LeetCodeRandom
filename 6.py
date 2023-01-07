from typing import List
from collections import Counter
from functools import reduce


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        """
        1338. Reduce Array Size to The Half
        :param arr:
        :return:
        """
        # TODO LATER (this is wrong)
        count = Counter(arr)
        sorted_keys = sorted(count, key=count.get, reverse=True)
        # print(count)
        # print(sorted_keys)

        ans = 0
        length = len(arr)
        for k in sorted_keys:
            if length - count[k] > len(arr) // 2:
                length -= count[k]
                del count[k]
                ans += 1
        return ans

    def findWords(self, words: List[str]) -> List[str]:
        """
        500. Keyboard Row
        :param words:
        :return:
        """
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'

        ans = []
        for word in words:
            if False not in [c in row1 for c in word.lower()] or False not in [c.lower() in row2 for c in
                                                                               word.lower()] or False not in [
                c.lower() in row3 for c in word.lower()]:
                ans.append(word)
        return ans

    def customSortString(self, order: str, s: str) -> str:
        """
        791. Custom Sort String
        :param order:
        :param s:
        :return:
        """
        ins, outs = [], []
        for c in s:
            if c in order:
                ins.append(c)
            else:
                outs.append(c)

        count = Counter(ins)
        ans = ''
        for o in order:
            ans += o * count[o]

        for o in outs:
            ans += o
        return ans

    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = []
        nums = [sorted(n) for n in nums]
        concat = list(set(reduce(list.__add__, nums)))
        for c in sorted(concat):
            if False not in [c in num for num in nums]:
                ans.append(c)
        return ans

    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        1636. Sort Array by Increasing Frequency
        :param nums:
        :return:
        """
        count = Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))




solution = Solution()

arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
# arr = [7, 7, 7, 7, 7, 7]
print(solution.minSetSize(arr))

words = ["Hello", "Alaska", "Dad", "Peace"]
print(solution.findWords(words))

order, s = "cbafg", "abcd"
order, s = "cba", "abcd"
# order, s ="kqep", "pekeq"
print(solution.customSortString(order, s))

nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
nums = [[1, 2, 3], [4, 5, 6]]
nums = [[7, 34, 45, 10, 12, 27, 13], [27, 21, 45, 10, 12, 13]]
print(solution.intersection(nums))

nums = [1, 1, 2, 2, 2, 3]
nums = [2, 3, 1, 3, 2]
print(solution.frequencySort(nums))

x = 123
x_reverse = int(str(x)[::-1])
print(x_reverse)
