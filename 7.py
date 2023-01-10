from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

    def longestSubarray(self, nums: List[int]) -> int:
        """
        1493. Longest Subarray of 1's After Deleting One Element
        :param nums:
        :return:
        """
        # TODO
        # hm = {}
        # l = 0
        #
        # for r in range(len(nums)):
        #     hm[nums[r]] = hm.get(nums[r], 0) + 1
        #     if hm.get(0, 0) > 1:
        #         hm.get(nums[l], 0) - 1
        #         l += 1
        #     # print(hm, l, r)
        # return r - l

    def isStrictlyPalindromic(self, n: int) -> bool:
        """
        2396. Strictly Palindromic Number
        :param n:
        :return:
        """

        def int2base(n, b):
            r = ""
            while n > 0:
                r += str(n % b)
                n //= b
            return int(r[-1::-1])

        for i in range(2, n - 1):
            print(int2base(n, i), n)
            if int2base(n, i) != n:
                print(False)
            else:
                print(True)
        #         return False
        # return True

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        2149. Rearrange Array Elements by Sign
        :param nums:
        :return:
        """
        # [3, 1, -2, -5, 2, -4]

        pos, neg = [], []
        for n in nums:
            if n > 0:
                pos.append(n)
            else:
                neg.append(n)
        ans = []
        for p, n in zip(pos, neg):
            ans.append(p)
            ans.append(n)
        return ans

    def minPairSum(self, nums: List[int]) -> int:
        """
        1877. Minimize Maximum Pair Sum in Array
        :param nums:
        :return:
        """
        # nums = [3, 5, 2, 3]
        mx = 0
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            mx = max(mx, nums[l] + nums[r])
            l += 1
            r -= 1
        return mx

    def partitionLabels(self, s: str) -> List[int]:
        """
        763. Partition Labels
        :param s:
        :return:
        """
        # TODO very simple but I still need to digest the logic
        ans = []
        hm = {}
        for i, v in enumerate(s):
            hm[v] = i

        l, r = 0, 0
        for i, v in enumerate(s):
            r = max(r, hm[v])
            if i == r:
                ans.append(r - l + 1)
                l = r + 1
        return ans

    def firstPalindrome(self, words: List[str]) -> str:
        """
        2108. Find First Palindromic String in the Array
        :param words:
        :return:
        """
        for w in words:
            if w == w[::-1]:
                return w
        return ''

    def reversePrefix(self, word: str, ch: str) -> str:
        """
        2000. Reverse Prefix of Word
        :param word:
        :param ch:
        :return:
        """
        try:
            r = word.index(ch)
            return word[:r + 1][::-1] + word[r + 1:]
        except ValueError:
            return word

    def removePalindromeSub(self, s: str) -> int:
        """
        1332. Remove Palindromic Subsequences
        :param s:
        :return:
        """
        return int(s == s[::-1]) or 2

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        905. Sort Array By Parity
        :param nums:
        :return:
        """
        # nums = [3, 1, 2, 4]
        ans = []
        for n in nums:
            if n % 2 == 0:
                ans.append(n)
        for n in nums:
            if n % 2 != 0:
                ans.append(n)
        return ans

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """876. Middle of the Linked List"""
        increment1 = increment2 = head
        while increment2 and increment2.next is not None:
            increment2 = increment2.next.next
            increment1 = increment1.next
        return increment1

    def shortestToChar(self, s: str, c: str) -> List[int]:
        """
        821. Shortest Distance to a Character
        """
        # s = "loveleetcode", c = "e"
        # [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
        indices = [i for i, v in enumerate(s) if v == c]
        ans = []
        for i in range(len(s)):
            if s[i] == c:
                ans.append(0)
            else:
                ans.append(min(abs(i - index) for index in indices))
        return ans

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """
        922. Sort Array By Parity II
        :param nums:
        :return:
        """
        evens = [n for n in nums if n % 2 == 0]
        odds = [n for n in nums if n % 2 != 0]
        ans = []
        for e, o in zip(evens, odds):
            ans.append(e)
            ans.append(o)
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

nums = [1, 1, 0, 1]
nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
print(solution.longestSubarray(nums))

n = 4
print(solution.isStrictlyPalindromic(n))

nums = [3, 1, -2, -5, 2, -4]
print(solution.rearrangeArray(nums))

nums = [3, 5, 2, 3]
print(solution.minPairSum(nums))

s = "ababcbacadefegdehijhklij"
print(solution.partitionLabels(s))

words = ["abc", "car", "ada", "racecar", "cool"]
print(solution.firstPalindrome(words))

word = "abcdefd"
ch = "d"
print(solution.reversePrefix(word, ch))

s = "ababa"
print(solution.removePalindromeSub(s))

nums = [3, 1, 2, 4]
print(solution.sortArrayByParity(nums))

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

print(solution.middleNode(head).val)

s, c = "loveleetcode", "e"
print(solution.shortestToChar(s, c))

nums = [4, 2, 5, 7]
print(solution.sortArrayByParityII(nums))

command = "G()(al)"
to_remov = {
    'G': 'G',
    '()': 'o',
    '(al)': 'al'
}
for char in to_remov.keys():
    print(char, to_remov[char])
    string = command.replace(char, to_remov[char])
print("Altered string: " + string)
