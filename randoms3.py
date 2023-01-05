from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        """
        1282. Group the People Given the Group Size They Belong To
        """
        count = defaultdict(list)
        for i, size in enumerate(groupSizes):
            count[size].append(i)

        # res = []
        # for k, v in count.items():
        #     for i in range(0, len(v), k):
        #         res.append(v[i: i + k])
        # return res
        return [v[i: i + k] for k, v in count.items() for i in range(0, len(v), k)]

    def decodeMessage(self, key: str, message: str) -> str:
        """
        2325. Decode the Message
        """
        hm = {}
        i = 97
        for k in key:
            if k.isalpha() and k not in hm:
                hm[k] = chr(i)
                i += 1

        ans = ''
        for m in message:
            if m in hm:
                ans += hm[m]
            else:
                ans += m
        return ans

    def checkIfPangram(self, sentence: str) -> bool:
        """
        1832. Check if the Sentence Is Pangram
        """
        count = {}
        for s in sentence:
            count[s] = count.get(s, 0) + 1
        for i in range(97, 97 + 26):
            if chr(i) not in count:
                return False
        return True

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        """
        2367. Number of Arithmetic Triplets
        """
        hs = set()
        for n in nums:
            if n + diff in nums and n + 2 * diff in nums:
                hs.add((n, n + diff, n + 2 * diff))
        return len(hs)

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        """
        804. Unique Morse Code Words
        """
        letter_to_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                          "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        codes = []
        for w in words:
            code = ''
            for c in w:
                code += letter_to_code[ord(c) - ord('a')]
            codes.append(code)

        count = {}
        for c in codes:
            count[c] = count.get(c, 0) + 1
        return len(count)

    def countKDifference(self, nums: List[int], k: int) -> int:
        """
        2006. Count Number of Pairs With Absolute Difference K
        """
        table = [(v, i) for i, v in enumerate(nums)]
        hs = set()
        for i, v in enumerate(nums):
            complement = v + k  # v - k also works
            for h in table:
                if h[0] == complement:
                    hs.add((h[1], i))
        return len(hs)

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
        1684. Count the Number of Consistent Strings
        """
        ans = 0
        for w in words:
            if len([c for c in w if c in allowed]) == len(w):
                ans += 1
        return ans

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        """
        2418. Sort the People
        """
        names_heights = list(zip(names, heights))
        names_heights.sort(key=lambda x: x[1], reverse=True)
        return [x[0] for x in names_heights]

    def countPoints(self, rings: str) -> int:
        """
        2103. Rings and Rods
        """
        count = defaultdict(list)
        for i in range(len(rings)):
            if rings[i].isnumeric():
                count[rings[i]].append(rings[i - 1])
        ans = 0
        for v in count.values():
            if len(set(v)) == 3:
                ans += 1
        return ans

    def detectCapitalUse(self, word: str) -> bool:
        """
        520. Detect Capital
        """
        # for l, w in zip(word.lower(), word):
        if True not in [lower == w for lower, w in zip(word.lower(), word)]:
            return True

        if word.lower() == word:
            return True

        if word[0].lower() != word[0] and word[1:].lower() == word[1:]:
            return True
        return False

    def intToRoman(self, num: int) -> str:
        """
        12. Integer to Roman
        """
        table = [(3000, 'MMM'), (2000, 'MM'), (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (300, 'CCC'),
                 (200, 'CC'), (100, 'C'), (90, 'XC'),
                 (50, 'L'), (40, 'XL'), (30, 'XXX'), (20, 'XX'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (3, 'III'),
                 (2, 'II'), (1, 'I')]
        ans = ''
        for i in range(len(table)):
            if table[i][0] <= num:
                ans += table[i][1]
                num -= table[i][0]
        return ans

    def romanToInt(self, s: str) -> int:
        """
        13. Roman to Integer
        """
        hm = {'MMM': 3000, 'MM': 2000, 'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'CCC': 300, 'CC': 200, 'C': 100,
              'XC': 90, 'L': 50, 'XL': 40, 'XXX': 30, 'XX': 20, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'III': 3, 'II': 2,
              'I': 1}
        ans = 0
        for k, v in hm.items():
            if s.startswith(k):
                ans += hm[k]
                s = s[len(k):]
        return ans

    def countDistinctIntegers(self, nums: List[int]) -> int:
        """
        2442. Count Number of Distinct Integers After Reverse Operations
        """

        reversed_n = [int(str(n)[::-1]) for n in nums]
        concat = nums + reversed_n

        count = {}
        for c in concat:
            count[c] = count.get(c, 0) + 1
        return len(count)

    def reverse(self, x: int) -> int:
        """
        7. Reverse Integer
        """
        if x < 0:
            reversed_int = - int(str(-x)[::-1])
            return reversed_int if reversed_int > -2 ** 31 else 0
        elif x > 0:
            reversed_int = int(str(x)[::-1])
            return reversed_int if reversed_int < 2 ** 31 - 1 else 0
        else:
            return 0

    def myAtoi(self, s: str) -> int:
        """
         String to Integer (atoi)
        """
        # TODO
        # string = ''
        # stripped = s.strip()
        # if stripped.startswith('+') or stripped.startswith('-'):
        #     for i in range(1, len(stripped)):
        #         string += stripped[i]
        #         if not stripped[i].isnumeric():
        #             break
        #     string = stripped[0] + string
        # else:
        #     for i in range(len(stripped)):
        #         string += stripped[i]
        #         if not stripped[i].isnumeric():
        #             break
        # return int(string)


solution = Solution()

groupSizes = [5, 5, 5, 5, 5, 1, 5]
groupSizes = [3, 3, 3, 3, 3, 1, 3]
print(solution.groupThePeople(groupSizes))

key, message = "the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"
# key, message = "eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
print(solution.decodeMessage(key, message))

sentence = "thequickbrownfoxjumpsoverthelazydog"
sentence = 'leetcode'
print(solution.checkIfPangram(sentence))

nums, diff = [0, 1, 4, 6, 7, 10], 3
print(solution.arithmeticTriplets(nums, diff))

words = ["gin", "zen", "gig", "msg"]
print(solution.uniqueMorseRepresentations(words))

nums, k = [3, 2, 1, 5, 4], 2
nums, k = [1, 2, 2, 1], 1
print(solution.countKDifference(nums, k))

allowed, words = "ab", ["ad", "bd", "aaab", "baa", "bada"]
print(solution.countConsistentStrings(allowed, words))

names, heights = ["Mary", "John", "Emma"], [180, 165, 170]
print(solution.sortPeople(names, heights))

rings = "B0R0G0R9R0B0G0"
print(solution.countPoints(rings))

word = "FlaG"
print(solution.detectCapitalUse(word))

num = 1994
print(solution.intToRoman(num))

s = "MCMXCIV"
print(solution.romanToInt(s))

nums = [1, 13, 10, 12, 31]
print(solution.countDistinctIntegers(nums))

x = 123
print(solution.reverse(x))

s = " -4193 with words"
print(solution.myAtoi(s))

