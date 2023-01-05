from typing import List, Optional
from collections import deque


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        5. Longest Palindromic Substring
        https://leetcode.com/problems/longest-palindromic-substring/
        """
        return 'TODO'

    def addBinary(self, a: str, b: str) -> str:
        """
        67. Add Binary
        """
        int_sum = int(a) + int(b)
        digits = deque([i for i in str(int_sum)])
        i = len(digits) - 1
        while i > 0:
            if int(digits[i]) >= 2:
                digits[i] = str(int(digits[i]) - 2)
                digits[i - 1] = str(int(digits[i - 1]) + 1)
            i -= 1

        if int(digits[0]) >= 2:
            digits[0] = str(int(digits[0]) - 2)
            digits.appendleft('1')
        return ''.join(digits)

    def mySqrt(self, x: int) -> int:
        """
        69. Sqrt(x)
        """
        # if x == 0:
        #     return 0
        # if x == 1 or x == 2:
        #     return 1
        # for i in range(x):
        #     if i * i > x:
        #         return i - 1
        if x < 2:
            return x
        l, r = 0, x // 2

        while l <= r:
            mid = (l + r) // 2
            if mid * mid > x:
                r = mid - 1
            elif mid * mid < x:
                l = mid + 1
            else:
                return mid
        return l - 1




s = Solution()

string = 'cbabcad'
print('5. Longest Palindromic Substring:', s.longestPalindrome(string))

a = "11"
b = "1"

a = "1010"
b = "1011"

a, b = '1111', '1111'

print('67. Add Binary:', s.addBinary(a, b))

x = 122
print('69. Sqrt(x): ', s.mySqrt(x))
