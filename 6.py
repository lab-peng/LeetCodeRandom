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

    def maxProfit(self, prices: List[int]) -> int:  # fixed sliding window of size 2
        """
        122. Best Time to Buy and Sell Stock II
        :param prices:
        :return:
        """
        # prices = [7, 1, 5, 3, 6, 4]
        max_profit = 0  # It's actually total profit
        for i in range(len(prices) - 1):
            profit = prices[i + 1] - prices[i] if prices[i + 1] > prices[i] else 0
            max_profit += profit
        return max_profit

    def countGoodSubstrings(self, s: str) -> int:
        """
        1876. Substrings of Size Three with Distinct Characters
        :param s:
        :return:
        """
        count = 0
        for i in range(len(s) - 2):
            if len(set(s[i: i + 3])) == len(s[i: i + 3]):
                count += 1
        return count

    def totalFruit(self, fruits: List[int]) -> int:
        """
        424. Longest Repeating Character Replacement
        :param fruits:
        :return:
        """
        # fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]  # 5
        # fruits = [1, 2, 3, 2, 2]  # 4
        l, total_fruit = 0, 0
        hm = {}
        for r in range(len(fruits)):
            hm[fruits[r]] = r
            if len(hm) > 2:
                min_val = min(hm.values())
                hm.pop(fruits[min_val])
                l = min_val + 1
            total_fruit = max(total_fruit, r - l + 1)
        return total_fruit

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        209. Minimum Size Subarray Sum
        :param target:
        :param nums:
        :return:
        """
        # target, nums = 7, [2, 3, 1, 2, 4, 3]
        l = 0
        sub_total = 0
        min_len = float('inf')
        for r in range(len(nums)):
            sub_total += nums[r]
            while sub_total >= target:
                # print(sub_total, l, r)
                min_len = min(min_len, r - l + 1)
                sub_total -= nums[l]
                l += 1
        return min_len if min_len != float('inf') else 0

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        567. Permutation in String
        :param s1:
        :param s2:
        :return:
        """
        # s1, s2 = "ab", "eidbaooo"
        # count_s1 = Counter(s1)
        # for i in range(len(s2) - len(s1) + 1):  # - window_size + 1
        #     window = s2[i: i + len(s1)]
        #     if Counter(window) == count_s1:
        #         return True
        # return False

        if len(s1) > len(s2):
            return False

        count_s1, count_s2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord("a")] += 1
            count_s2[ord(s2[i]) - ord("a")] += 1
        # print(count_s1, count_s2)

        matches = 0
        for i in range(26):
            matches += 1 if count_s1[i] == count_s2[i] else 0
        # print(matches)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            count_s2[index] += 1
            if count_s1[index] == count_s2[index]:
                matches += 1
            elif count_s1[index] + 1 == count_s2[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            count_s2[index] -= 1
            if count_s1[index] == count_s2[index]:
                matches += 1
            elif count_s1[index] - 1 == count_s2[index]:
                matches -= 1
            l += 1
        return matches == 26

    def maxSubArray(self, nums: List[int]) -> int:
        current, _max = 0, nums[0]

        for num in nums:
            current = max(current + num, num)
            _max = max(_max, current)

        return _max



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

prices = [7, 1, 5, 3, 6, 4]
prices = [1, 2, 3, 4, 5]
prices = [7, 6, 4, 3, 1]
print(solution.maxProfit(prices))

s = "aababcabc"
print(solution.countGoodSubstrings(s))

fruits = [1, 2, 3, 2, 2]  # 4
fruits = [0, 1, 2, 2]  # 3
fruits = [1, 2, 1]  # 3
fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]  # 5
print(solution.totalFruit(fruits))

target, nums = 7, [2, 3, 1, 2, 4, 3]
print(solution.minSubArrayLen(target, nums))

s1, s2 = "ab", "eidbaooo"
# s1, s2 = 'adc', 'dcda'
print(solution.checkInclusion(s1, s2))

nums = [-3, -2, -1]
print(solution.maxSubArray(nums))
