from typing import List
from collections import Counter


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
        print(count)
        print(sorted_keys)


        ans = 0
        length = len(arr)
        for k in sorted_keys:
            if length - count[k] > len(arr) // 2:
                length -= count[k]
                del count[k]
                ans += 1

        print(length)
        return ans

    def findWords(self, words: List[str]) -> List[str]:
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'

        ans = []
        for word in words:
            if [c in row1 for c in words]





solution = Solution()

arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
# arr = [7, 7, 7, 7, 7, 7]
print(solution.minSetSize(arr))
