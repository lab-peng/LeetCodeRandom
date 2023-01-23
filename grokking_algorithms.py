import random
from typing import List


# Suppose you’re a farmer with a plot of land. You want to divide this farm evenly into square plots. You want the plots
# to be as big as possible. So none of these will work. How do you figure out the largest square size you can use for a plot of land?

def find_biggest_square(width, height):
    if width % height == 0:
        return height
    return find_biggest_square(height, width % height)


print(find_biggest_square(1680, 640))  # 80
print(find_biggest_square(64,
                          168))  # 8   64 % 168 = 64 => find_biggest_square(168, 64) => It will swap the width and height
print(find_biggest_square(50, 25))  # 25


def merge_sort(nums):
    if len(nums) > 1:
        m = len(nums) // 2
        left = nums[:m]
        right = nums[m:]

        # print(left, right)
        merge_sort(left)
        merge_sort(right)

        l, r, i = 0, 0, 0  # left, right, index
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                nums[i] = left[l]
                l += 1
            else:
                nums[i] = right[r]
                r += 1
            i += 1

        while l < len(left):
            nums[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            nums[i] = right[r]
            r += 1
            i += 1


random.seed(1000)
numbers = [random.randint(0, 1000) for _ in range(10)]
print(numbers)
print(sorted(numbers))

merge_sort(numbers)
print(numbers)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # l, r = 0, len(nums) - 1

        # while l <= r:
        #     m = (l + r) // 2
        #     if target == nums[m]:
        #         return m
        #     if target > nums[m]:
        #         l = m + 1
        #     else:
        #         r = m - 1
        # return l

        l, r = 0, len(nums)

        while l < r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            else:
                r = m

        return l


nums = [1, 3, 5, 6]
target = 5
s = Solution()
print(s.searchInsert(nums, target))
