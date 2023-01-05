from collections import defaultdict, Counter
from typing import List
from itertools import zip_longest, combinations


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        p = Solution.make_pattern(pattern)
        return [w for w in words if Solution.make_pattern(w) == p]

    @staticmethod
    def make_pattern(w):
        hm, array, count = {}, [], 0
        for c in w:
            if c not in hm:
                hm[c] = count
                count += 1
            array.append(hm[c])
        return array

    def minSteps(self, s: str, t: str) -> int:
        diff = Counter(s) - Counter(t)
        return sum(diff.values())

    def destCity(self, paths: List[List[str]]) -> str:
        """
        1436. Destination City
        """
        hm = {p[0]: p[1] for p in paths}
        for k, v in hm.items():
            if v not in hm:
                return v

    def numberOfPairs(self, nums: List[int]) -> List[int]:
        """
        2341. Maximum Number of Pairs in Array
        :param nums:
        :return:
        """
        # count = {}
        # for n in nums:
        #     count[n] = count.get(n, 0) + 1
        count = Counter(nums)
        ans = [0, 0]
        # print(count.values())
        for v in count.values():
            ans[0] += v // 2
            ans[1] += v % 2
        return ans

    def repeatedNTimes(self, nums: List[int]) -> int:
        """
        961. N-Repeated Element in Size 2N Array
        :param nums:
        :return:
        """
        count = Counter(nums)
        for k, v in count.items():
            if v == len(nums) / 2:
                return k

    def sumOfUnique(self, nums: List[int]) -> int:
        """
        1748. Sum of Unique Elements
        :param nums:
        :return:
        """
        count = Counter(nums)
        return sum([k for k, v in count.items() if v == 1])

    def repeatedCharacter(self, s: str) -> str:
        """
        2351. First Letter to Appear Twice
        :param s:
        :return:
        """
        least = float('inf')
        count = defaultdict(list)
        for i, v in enumerate(s):
            count[v].append(i)
        for v in count.values():
            if len(v) > 1:
                print(v[1])
                least = min(least, v[1])
        return s[least]

    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        """

        :param items1:
        :param items2:
        :return:
        """
        return sorted((Counter(dict(items1)) + Counter(dict(items2))).items())

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        """
        811. Subdomain Visit Count
        :param cpdomains:
        :return:
        """
        hm = defaultdict(int)
        for cpd in cpdomains:
            pair = cpd.split(' ')
            pair[1] = pair[1].split('.')
            for i in range(len(pair[1])):
                hm[tuple(pair[1][i:])] += int(pair[0])
        return [f"{str(v)} {'.'.join(k)}" for k, v in hm.items()]

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        """
        812. Largest Triangle Area
        :param points:
        :return:
        """

        def area_cal(corr1, corr2, corr3):
            (x1, y1), (x2, y2), (x3, y3) = corr1, corr2, corr3
            return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

        return max(area_cal(corr1, corr2, corr3) for corr1, corr2, corr3 in combinations(points, 3))

    def partitionString(self, s: str) -> int:
        """
        2405. Optimal Partition of String
        :param s:
        :return:
        """
        # TODO:  I don't understand the problem
        hs = set()
        ans = 1
        for c in s:
            if c in hs:
                ans += 1
                hs = set()
            hs.add(c)
            print(hs)
        return ans


solution = Solution()

words, pattern = ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "xyy"
print(solution.findAndReplacePattern(words, pattern))

s, t = "leetcode", "practice"
print(solution.minSteps(s, t))

paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
print(solution.destCity(paths))

nums = [1, 3, 2, 1, 3, 2, 2]
# nums = [1, 1]
# nums = [0, 0, 1]
print(solution.numberOfPairs(nums))

nums = [5, 1, 5, 2, 5, 3, 5, 4]
# nums = [1, 2, 3, 3]
print(solution.repeatedNTimes(nums))

s = "abccbaacz"
print(solution.repeatedCharacter(s))

items1, items2 = [[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]]
items1, items2 = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5]], [[7, 1], [6, 2], [5, 3], [4, 4]]
items1, items2 = [[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]]
print(solution.mergeSimilarItems(items1, items2))

cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(solution.subdomainVisits(cpdomains))

points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
points = [[1, 0], [0, 0], [0, 1]]
print(solution.largestTriangleArea(points))

s = "abacaba"
s = 'ab'
print(solution.partitionString(s))