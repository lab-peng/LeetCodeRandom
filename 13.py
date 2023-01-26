import heapq
import random
import statistics
from bisect import bisect_right
from collections import deque, defaultdict, Counter
from itertools import accumulate, starmap, zip_longest
from operator import sub
from typing import List


# from collections import Counter
# bank = ["011001", "000000", "000000", "010100", "001000"]
# bank = [Counter(b) for b in bank]
# print(bank)
#
# l, r = 0, 1
# ans = 0
# while r < len(bank):
#     while r < '1' not in bank[r]:
#         r += 1
#     if l != r:
#         ans += bank[l].get('1') * bank[r].get('1')
#     l = r
#     r += 1
#
#
#
# # for r in range(1, len(bank)):
# #     while '1' not in bank[r]:
# #         r += 1
# #     if l != r:
# #         # ans += bank[l].get('1') * bank[r].get('1')
# #         print(l, r)
# #     l = r
# #
# print(ans)

class Solution:
    def maxDepth(self, s: str) -> int:
        """
        1614. Maximum Nesting Depth of the Parentheses
        """
        hm = {
            ')': '('
        }
        stack = []
        max_depth = float('-inf')

        for c in s:
            if c not in '()':
                continue
            if c not in hm:
                stack.append(c)
                continue
            # if not stack or stack[-1] != hm[c]:
            #     return False
            # print(stack)
            max_depth = max(max_depth, len(stack))
            stack.pop()

        return max_depth


s = "(1+(2*3)+((8)/4))+1"
solution = Solution()
print(solution.maxDepth(s))


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        """
        1630. Arithmetic Subarrays
        https://leetcode.com/problems/arithmetic-subarrays/
        """

        def is_sq(arr):
            diff = arr[1] - arr[0]
            for i in range(len(arr) - 1):
                if arr[i + 1] - arr[i] != diff:
                    return False
            return True

        ans = []
        for start, end in zip(l, r):
            sub_nums = sorted(nums[start: end + 1])
            ans.append(is_sq(sub_nums))

        return ans


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        """
        1561. Maximum Number of Coins You Can Get
        https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
        """
        piles.sort(reverse=True)
        l, r = 0, len(piles) - 1
        ans = 0
        while l + 1 < r:
            # print(piles[l], piles[l + 1], piles[r])
            ans += piles[l + 1]
            l += 2
            r -= 1
        return ans


piles = [9, 8, 7, 6, 5, 1, 2, 3, 4]

s = Solution()
print(s.maxCoins(piles))


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        """
        950. Reveal Cards In Increasing Order
        https://leetcode.com/problems/reveal-cards-in-increasing-order/
        """
        # todo: I haven't figured out the logic
        size = len(deck)
        indices = deque(range(size))
        # print(indices)
        ans = [0] * size

        for card in sorted(deck):
            ans[indices.popleft()] = card
            if indices:
                indices.append(indices.popleft())
        return ans


deck = [17, 13, 11, 2, 3, 5, 7]
# Output: [2,13,3,11,5,17,7]
s = Solution()
print(s.deckRevealedIncreasing(deck))


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        """
        1418. Display Table of Food Orders in a anstaurant
        https://leetcode.com/problems/display-table-of-food-orders-in-a-anstaurant/
        """
        tables_foods = sorted(orders, key=lambda x: int(x[1]))
        foods = sorted(orders, key=lambda x: x[2])

        tables_foods_hm = defaultdict(int)
        tables_hm = {}
        for tf in tables_foods:
            tables_hm[tf[1]] = 0
            tables_foods_hm[tf[1], (tf[2])] += 1

        foods_hm = {}
        for f in foods:
            foods_hm[f[2]] = 0

        ans = [['Table']]
        for food in foods_hm:
            ans[0].append(food)

        for table in tables_hm:
            table_lst = [table]
            for food in foods_hm:
                table_lst.append(str(tables_foods_hm[(table, food)]))

            ans.append(table_lst)
        return ans


orders = [["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
          ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]
s = Solution()
print(s.displayTable(orders))


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        """
        2545. Sort the Students by Their Kth Score
        https://leetcode.com/problems/sort-the-students-by-their-kth-score/
        """
        return sorted(score, key=lambda x: x[k], reverse=True)


score = [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]]
k = 2

s = Solution()
print(s.sortTheStudents(score, k))


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        """
        1637. Widest Vertical Area Between Two Points Containing No Points
        https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
        """
        points.sort()
        widest = 0
        for i in range(1, len(points)):
            widest = max(widest, points[i][0] - points[i - 1][0])
        return widest


points = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
s = Solution()
print(s.maxWidthOfVerticalArea(points))

print("Python printing tricks: ")


def fib(x):
    fibs = [0] * (x + 1)
    if x > 0:
        fibs[1] = 1
        fibs = [0, 1] + [0] * (x - 1)
        for i in range(2, len(fibs)):
            fibs[i] = fibs[i - 1] + fibs[i - 2]
    return fibs[x]


for i in range(100):
    print(f'{fib(i):,}', end='  ')


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        """
        2037. Minimum Number of Moves to Seat Everyone
        https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
        """
        seats.sort()
        students.sort()

        ans = 0
        for seat, student in zip(seats, students):
            ans += abs(seat - student)
        return ans


print()
seats = [3, 1, 5]
students = [2, 7, 4]
s = Solution()
print(s.minMovesToSeat(seats, students))


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        406. Queue Reconstruction by Height
        https://leetcode.com/problems/queue-reconstruction-by-height/
        """
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        for p in people:
            ans.insert(p[1], p)
        return ans


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
s = Solution()
print(s.reconstructQueue(people))


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # accumulates = []
        # crt_total = 0
        # for n in sorted(nums):
        #     crt_total += n
        #     accumulates.append(crt_total)
        # return [len([x for x in accumulates if x <= q]) for q in queries]
        accumulates = list(accumulate(sorted(nums)))
        return [bisect_right(accumulates, q) for q in queries]


nums = [1, 2, 4, 5]
queries = [3, 10, 21]
s = Solution()
print(s.answerQueries(nums, queries))


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        """
        1356. Sort Integers by The Number of 1 Bits
        https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
        """
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
s = Solution()
print(s.sortByBits(arr))


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """
        1337. The K Weakest Rows in a Matrix
        https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
        """
        # sorted_mat = (sorted([(idx, row.count(1)) for idx, row in enumerate(mat)], key=lambda x: x[1]))
        # return [x[0] for x in sorted_mat[:k]]
        return [x[1] for x in heapq.nsmallest(k, ((row.count(1), idx) for idx, row in enumerate(mat)))]


mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]
k = 3

s = Solution()
print(s.kWeakestRows(mat, k))


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        """
        1403. Minimum Subsequence in Non-Increasing Order
        https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/
        """
        sorted_nums = sorted(nums, reverse=True)
        total = sum(sorted_nums)
        left = 0
        ans = []
        for n in sorted_nums:
            left += n
            right = total - left
            ans.append(n)
            if left > right:
                break
        return ans


nums = [4, 3, 10, 9, 8]
s = Solution()
print(s.minSubsequence(nums))


class Solution:
    """
    1402. Reducing Dishes
    https://leetcode.com/problems/reducing-dishes/
    """

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # satisfaction = sorted(satisfaction)
        # max_s = 0
        # for i in range(len(satisfaction)):
        #     total = 0
        #     for j in range(i, len(satisfaction)):
        #         total += (j - i + 1) * satisfaction[j]
        #     max_s = max(max_s, total)
        # return max_s

        # satisfaction = sorted(satisfaction, reverse=True)
        # crt_sum = 0
        # total = 0
        # for s in satisfaction:
        #     crt_sum += s
        #     if crt_sum < 0:
        #         break
        #     total += crt_sum
        # return total

        # Insight: [2, 3, 4] 2*1 + 3*2 + 4*3 ==  list(accumulate(list(accumulate([4, 3, 2]))))

        satisfaction.sort(reverse=True)
        ans = 0
        running_sum = accumulate(satisfaction)  # Using accumulate seems increasing time efficiency
        for r in running_sum:
            if r < 0:
                break
            ans += r
        return ans


satisfaction = [-1, -8, 0, 5, -9]
satisfaction = [4, 3, 2, -8]
# satisfaction = [-1, -4, -5]

s = Solution()
print(s.maxSatisfaction(satisfaction))


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        """
        1387. Sort Integers by The Power Value
        https://leetcode.com/problems/sort-integers-by-the-power-value/
        """
        # def power_val(x):
        #     steps = 0
        #     crt = x
        #     while crt != 1:
        #         if crt % 2 == 0:
        #             crt = crt / 2
        #         else:
        #             crt = crt * 3 + 1
        #         steps += 1
        #     return steps
        # # int_list = [(power_val(i), i) for i in range(lo, hi + 1)]
        # return heapq.nsmallest(k, [(power_val(i), i) for i in range(lo, hi + 1)])[-1][1]

        # Insight: sort or heapq with a custom function is slow ?

        ans = []
        for i in range(lo, hi + 1):
            steps = 0
            crt_val = i
            while crt_val != 1:
                if crt_val % 2 == 0:
                    crt_val = crt_val // 2
                else:
                    crt_val = 3 * crt_val + 1
                steps += 1
            ans.append([i, steps])

        ans.sort(key=lambda x: x[1])

        ans = ans[k - 1]
        return ans[0]


lo, hi, k = 7, 11, 4
lo, hi, k = 12, 15, 2
s = Solution()
print(s.getKth(lo, hi, k))


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        """
        969. Pancake Sorting
        https://leetcode.com/problems/pancake-sorting/
        https://leetcode.com/problems/pancake-sorting/discussion/comments/1564957/
        """

        def flip(r):
            l = 0
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        ans = []
        for i in range(len(arr) - 1, 0, -1):
            max_idx = arr.index(max(arr[:i + 1]))

            flip(max_idx)
            if max_idx != 0:
                ans.append(max_idx + 1)

            flip(i)
            ans.append(i + 1)
        return ans


arr = [3, 2, 4, 1]
arr = [1, 2, 3]
s = Solution()
print(s.pancakeSort(arr))


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        """
        1338. Reduce Array Size to The Half
        https://leetcode.com/problems/reduce-array-size-to-the-half/
        """

        count = Counter(arr)
        count = sorted(count.values(), reverse=True)
        size = len(arr)
        sub_size = 0
        ans = 0
        for c in count:
            ans += 1
            sub_size += c
            if sub_size >= size // 2:
                break
        return ans


arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
s = Solution()
print(s.minSetSize(arr))


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        """
        1433. Check If a String Can Break Another String
        https://leetcode.com/problems/check-if-a-string-can-break-another-string/
        """
        s1, s2 = list(s1), list(s2)
        s1.sort()
        s2.sort()
        return all(a >= b for a, b in zip(s1, s2)) or all(b >= a for b, a in zip(s2, s1))


s1, s2 = "abc", "xya"
# s1, s2 = "abe", "acd"
# s1, s2 = 'leetcodee', 'interview'

s = Solution()
print(s.checkIfCanBreak(s1, s2))


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        1122. Relative Sort Array
        https://leetcode.com/problems/relative-sort-array/
        """
        # head = [a for a in arr1 if a in arr2]
        # tail = [a for a in arr1 if a not in arr2]
        # ans = []
        # count = Counter(head)
        # for a in arr2:
        #     for i in range(count[a]):
        #         ans.append(a)
        # return ans + sorted(tail)

        return sorted(arr1, key=(arr2 + sorted(arr1)).index)


# arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
# arr2 = [2, 1, 4, 3, 9, 6]

arr1 = [28, 6, 22, 8, 44, 17]
arr2 = [22, 28, 8, 6]
s = Solution()
print(s.relativeSortArray(arr1, arr2))


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        """
        2279. Maximum Bags With Full Capacity of Rocks
        https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
        """

        # diff = sorted([c - r for c, r in zip(capacity, rocks)])
        diff = sorted(starmap(sub, zip(capacity, rocks)))  # faster version with python in-built functions

        # ans = 0
        # for d in diff:
        #     additionalRocks -= d
        #     if additionalRocks < 0:
        #         break
        #     ans += 1
        # return ans

        return bisect_right(list(accumulate(diff)), additionalRocks)  # faster version with python in-built functions


capacity = [2, 3, 4, 5]
rocks = [1, 2, 4, 4]
additionalRocks = 2

s = Solution()
print(s.maximumBags(capacity, rocks, additionalRocks))


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # evens = sorted([nums[i] for i in range(len(nums)) if i % 2 == 0])
        # odds = sorted([nums[i] for i in range(len(nums)) if i % 2 != 0], reverse=True)
        # ans = []
        # for e, o in zip_longest(evens, odds):
        #     ans.append(e)
        #     if o:
        #         ans.append(o)
        # return ans

        nums[::2], nums[1::2] = sorted(nums[::2]), sorted(nums[1::2])[::-1]  # faster version
        return nums


nums = [5, 39, 33, 5, 12, 27, 20, 45, 14, 25, 32, 33, 30, 30, 9, 14, 44, 15, 21]
s = Solution()
print(s.sortEvenOdd(nums))


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        """
        1619. Mean of Array After Removing Some Elements
        https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
        """
        arr.sort()
        size = len(arr)
        percent = int(size * 0.05)
        # return sum(arr[percent: -percent]) / (size - percent * 2)
        return statistics.mean(arr[percent: -percent])


arr = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]

s = Solution()
print(s.trimMean(arr))
