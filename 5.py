import math
from typing import List
from collections import Counter, defaultdict
from itertools import zip_longest


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        """
        2206. Divide Array Into Equal Pairs
        :param nums:
        :return:
        """
        count = Counter(nums)
        for v in count.values():
            if v % 2 != 0:
                return False

        return True

    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        """
        1418. Display Table of Food Orders in a Restaurant
        :param orders:
        :return:
        """
        return 'No answer so far!'
        # TODO
        # hm = defaultdict(list)
        # name_set = set()
        # food_set = set()
        # for name, table_num, food in orders:
        #     print(name, table_num, food)
        #     if name not in name_set:
        #         name_set.add(name)
        #     if food not in food_set:
        #         food_set.add(food)
        #
        #     hm[table_num].append(food)
        # print(hm)
        # print(name_set, food_set)

    def digitCount(self, num: str) -> bool:
        count = Counter(num)
        for i, v in enumerate(num):
            if count.get(str(i), 0) != int(v):
                return False
        return True

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        """
        2225. Find Players With Zero or One Losses
        """
        ans = [[], []]
        winners, losers = set(), {}
        for w, l in matches:
            winners.add(w)
            losers[l] = losers.get(l, 0) + 1
        for w in sorted(winners):
            if w not in losers:
                ans[0].append(w)
        ans[1] = sorted([k for k, w in losers.items() if w == 1])
        return ans

    def findFinalValue(self, nums: List[int], original: int) -> int:
        """
        Keep Multiplying Found Values by Two
        :param nums:
        :param original:
        :return:
        """
        while original in nums:
            original *= 2
        return original

    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ans = []
        for n in set(nums1) | set(nums2) | set(nums3):
            if (n in nums1 and n in nums2) or (n in nums1 and n in nums3) or (n in nums2 and n in nums3):
                ans.append(n)
        return ans

    def minimumOperations(self, nums: List[int]) -> int:
        """
        2357. Make Array Zero by Subtracting Equal Amounts
        :param nums:
        :return:
        """
        ans = 0
        while not all(item <= 0 for item in nums):
            # get the min except 0
            min_n = float('inf')
            for n in nums:
                if n != 0:
                    min_n = min(min_n, n)

            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] -= int(min_n)
            ans += 1
            # print(ans, nums, min_n)
        return ans

    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        return sum((count_s - count_t).values()) + sum((count_t - count_s).values())

    def kthDistinct(self, arr: List[str], k: int) -> str:
        """
        2053. Kth Distinct String in an Array
        :param arr:
        :param k:
        :return:
        """
        count = Counter(arr)
        i = 0
        for a in arr:
            if count[a] == 1:
                i += 1
            if i == k:
                return a
        return ""

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        496. Next Greater Element I
        :param nums1:
        :param nums2:
        :return:
        """
        ans = []
        for i, j in zip(nums1, nums2):
            if (nums2.index(i) + 1 < len(nums2) - 1) and nums2[nums2.index(i) + 1] > i:
                ans.append(nums2[nums2.index(i) + 1])
            else:
                ans.append(-1)
        return ans

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        1935. Maximum Number of Words You Can Type
        :param text:
        :param brokenLetters:
        :return:
        """
        text = text.split(' ')
        ans = len(text)
        for t in text:
            if set(brokenLetters) & set(t):
                ans -= 1

        return ans

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        2215. Find the Difference of Two Arrays
        :param nums1:
        :param nums2:
        :return:
        """
        return [list(set(nums1).difference(set(nums2))), list(set(nums2).difference(set(nums1)))]

    def countWords(self, words1: List[str], words2: List[str]) -> int:
        """
        2085. Count Common Words With One Occurrence
        :param words1:
        :param words2:
        :return:
        """
        ans = 0
        count1, count2 = Counter(words1), Counter(words2)
        for k in set(count1.keys()).intersection(set(count2.keys())):
            if count1[k] == count2[k] == 1:
                ans += 1
        return ans

    def similarPairs(self, words: List[str]) -> int:
        """
        2506. Count Pairs Of Similar Strings
        NOTE: Frozenset is hashable while ordinary set isn't.
        """
        words = [frozenset(w) for w in words]
        count = Counter(words)
        k_in_n_combination = lambda k, n: math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
        return int(sum([k_in_n_combination(2, h) for h in count.values() if h > 1]))


solution = Solution()

nums = [3, 2, 3, 2, 2, 2]
print(solution.divideArray(nums))

orders = [["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
          ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]
orders = [["James", "12", "Fried Chicken"], ["Ratesh", "12", "Fried Chicken"], ["Amadeus", "12", "Fried Chicken"],
          ["Adam", "1", "Canadian Waffles"], ["Brianna", "1", "Canadian Waffles"]]
orders = [["Laura", "2", "Bean Burrito"], ["John", "2", "Beef Burrito"], ["Melissa", "2", "Soda"]]
print(solution.displayTable(orders))

num = "1210"
print(solution.digitCount(num))

matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
# matches = [[2, 3], [1, 3], [5, 4], [6, 4]]
print(solution.findWinners(matches))

nums = [5, 3, 6, 1, 12]
original = 3
print(solution.findFinalValue(nums, original))

nums1 = [1, 1, 3, 2]
nums2 = [2, 3]
nums3 = [3]
print(solution.twoOutOfThree(nums1, nums2, nums3))

nums = [1, 5, 0, 3, 5]
# nums = [5, 3, 2, 1]
# nums = [0, 4, 0, 2, 4]
print(solution.minimumOperations(nums))

s = "leetcode"
t = "coats"
print(solution.minSteps(s, t))

arr, k = ["d", "b", "c", "b", "c", "a"], 2
# arr, k = ["a", "b", "a"], 3

print(solution.kthDistinct(arr, k))

nums1, nums2 = [2, 4], [1, 2, 3, 4]
print(solution.nextGreaterElement(nums1, nums2))

text, brokenLetters = "leet code", "lt"
print(solution.canBeTypedWords(text, brokenLetters))

nums1, nums2 = [1, 2, 3], [2, 4, 6]
print(solution.findDifference(nums1, nums2))

words1, words2 = ["leetcode", "is", "amazing", "as", "is"], ["amazing", "leetcode", "is"]
print(solution.countWords(words1, words2))

words = ["aba", "aabb", "abcd", "bac", "aabc"]
# words = ["aabb","ab","ba"]
# words = ["nba","cba","dba"]
print(solution.similarPairs(words))


