"""
Reorganize String — LeetCode 767
https://leetcode.com/problems/reorganize-string/description/

Logic:
    Count character frequencies, then build a max-heap of (negative_count, char).
    At each step, pop the most frequent character, append it to the result, and
    hold it as "prev". On the next iteration, push prev back if its count > 0,
    ensuring the same character is never placed consecutively.

Time:  O(n log k) — n characters appended, each requiring a heap op; k ≤ 26
Space: O(k) — heap holds at most 26 distinct characters
"""

from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [[-ct, char] for char, ct in count.items()]
        heapq.heapify(max_heap)
        prev = None
        res = ""
        while max_heap or prev:
            if prev and not max_heap:
                return ""

            ct, char = heapq.heappop(max_heap)
            res += char
            ct +=1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            if ct != 0:
                prev =[ct, char]

        return res

if __name__ == '__main__':
    s = "aaab"
    S = Solution()
    print("Input: {}, OutPut : {}".format(s,S.reorganizeString(s)))
    s = "aab"
    S = Solution()
    print("Input: {}, OutPut : {}".format(s,S.reorganizeString(s)))