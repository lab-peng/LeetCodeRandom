from typing import List, Optional


class Solution:
    # def isValid(self, s: str) -> bool:
    #     """
    #     20. Valid Parentheses
    #     https://leetcode.com/problems/valid-parentheses/
    #     """
    #     hm = {
    #         ')': '(',
    #         '}': '{',
    #         ']': '['
    #     }
    #
    #     stack = []
    #     for c in s:
    #         if c in hm:
    #             if stack and stack[-1] == hm[c]:
    #                 stack.pop()
    #             else:
    #                 return False
    #         else:
    #             stack.append(c)
    #
    #     return not stack

    def isValid(self, s: str) -> bool:
        """
        20. Valid Parentheses
        https://leetcode.com/problems/valid-parentheses/
        """
        hm = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for c in s:
            if hm.get(c):
                stack.append(c)
            else:
                if stack and hm[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return not stack

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1. Two Sum
        https://leetcode.com/problems/two-sum/
        """
        hm = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] in hm:
                return [hm[nums[i]], i]
            else:
                hm[complement] = i
        return -1

    def maxProfit(self, prices: List[int]) -> int:
        """
        121. Best Time to Buy and Sell Stock
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
        """
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return max_profit

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        26. Remove Duplicates from Sorted Array
        https://leetcode.com/problems/remove-duplicates-from-sorted-array/
        """
        if not nums:
            return 1

        l = r = 1
        while r < len(nums):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
            r += 1

        return l

    def removeElement(self, nums: List[int], val: int) -> int:
        """
        27. Remove Element
        https://leetcode.com/problems/remove-element/
        """
        l = r = 0
        while r < len(nums):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l

    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        35. Search Insert Position
        https://leetcode.com/problems/search-insert-position/
        """
        nums.append(float('inf'))

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            else:
                r = m
        return l

    def lengthOfLastWord(self, s: str) -> int:
        """
        58. Length of Last Word
        https://leetcode.com/problems/length-of-last-word/
        """
        s = s.strip()
        last_len = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                break
            last_len += 1
        return last_len

    def plusOne(self, digits: List[int]) -> List[int]:
        """
        66. Plus One
        https://leetcode.com/problems/plus-one/
        """
        # if digits[-1] == 9:
        #     digits.append(10)
        #     i = len(digits) - 1
        #     while i > 0:
        #         if digits[i] == 10:
        #             digits[i] = 0
        #             digits[i - 1] += 1
        #         i -= 1
        #     if digits[0] == 10:
        #         digits[0] = 1
        #     else:
        #         digits.pop()
        # else:
        #     digits[-1] += 1
        # return digits

        integer = int(''.join([str(d) for d in digits])) + 1
        return [int(d) for d in str(integer)]

    def strStr(self, haystack: str, needle: str) -> int:
        """
        28. Find the Index of the First Occurrence in a String
        https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
        """
        n_len = len(needle)
        for i in range(len(haystack)):
            if needle == haystack[i: i+n_len]:
                return i
        return -1

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        3. Longest Substring Without Repeating Characters
        https://leetcode.com/problems/longest-substring-without-repeating-characters/
        """
        char_set = set()
        l, r = 0, 0
        max_len = 0

        while r < len(s):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len



s = Solution()

x = "()"
x = "()[]{}"
# x = "{[]}()"
# x = "(]"
print('Valid Parentheses:', s.isValid(x))

nums, target = [2, 7, 11, 15], 22
nums, target = [3, 2, 4], 6
print('Two Sum:', s.twoSum(nums, target))

prices = [7, 1, 5, 3, 6, 4]
print('Best Time to Buy and Sell Stock:', s.maxProfit(prices))

nums = [1, 1, 2]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums = []
nums = [1, 2, 2, 3, 6, 6, 6, 7, 8]
print('Remove Duplicates from Sorted Array:', s.removeDuplicates(nums), nums)

nums, val = [3, 2, 2, 3], 3
nums, val = [0, 1, 2, 2, 3, 0, 4, 2], 2
print('Remove Element: ', s.removeElement(nums, val), nums)

nums, target = [1, 3, 7, 8], 6
print('Search Insert Position:', s.searchInsert(nums, target))

string = 's World  '
print('Length of Last Word:', s.lengthOfLastWord(string))

x = [9, 9, 9]

print('Plus One:', s.plusOne(x))


haystack = "sadbutsad"
needle = "sad"
# haystack = "leetcode"
# needle = "leeto"

print('Find the Index of the First Occurrence in a String:', s.strStr(haystack, needle))

string = "abcabcbb"
string = "pwwkew"
print('Longest Substring Without Repeating Characters:', s.lengthOfLongestSubstring(string))