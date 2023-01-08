from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        881. Boats to Save People
        :param people:
        :param limit:
        :return:
        """
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            boats += 1
            r -= 1
        return boats

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
        :param arr:
        :param k:
        :param threshold:
        :return:
        """
        # arr = [2, 2, 2, 2, 5, 5, 5, 8]
        # k = 3
        # threshold = 4

        window_sum = sum(arr[:k])
        ans = 1 if window_sum / k >= threshold else 0  # The first window
        for i in range(k, len(arr)):
            window_sum += arr[i]
            window_sum -= arr[i - k]
            if window_sum / k >= threshold:
                ans += 1
        return ans

    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        1004. Max Consecutive Ones III
        :param nums:
        :param k:
        :return:
        """
        # nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2
        count = {}
        l = 0
        for r in range(len(nums)):
            count[nums[r]] = count.get(nums[r], 0) + 1
            if count.get(0, 0) > k:
                count[nums[l]] -= 1
                l += 1
        return r - l + 1

    def numberOfSubstrings(self, s: str) -> int:
        """
        1358. Number of Substrings Containing All Three Characters
        :param s:
        :return:
        """
        # s = "aaacb"
        # TODO don't know why it does NOT work
        count = {}
        l = 0
        ans = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            if len(count) == 3:
                if count.get(s[l]) > 1:
                    count[s[l]] -= 1
                else:
                    count.pop(s[l])
                l += 1
                ans += 1
            # print(l, r, ans, count, len(count) == 3)
        return ans


solution = Solution()

people, limit = [1, 2, 2, 3], 3
print(solution.numRescueBoats(people, limit))

arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4

arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
k = 3
threshold = 5
print(solution.numOfSubarrays(arr, k, threshold))

nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 3
print(solution.longestOnes(nums, k))

s = "aaacb"
print(solution.numberOfSubstrings(s))


