"""
IPO — LeetCode 502
https://leetcode.com/problems/ipo/description/

Logic:
    Use two heaps: a min-heap sorted by capital requirement and a max-heap sorted
    by profit (negated). In each of k rounds, push all projects whose capital ≤ w
    onto the max-heap, then greedily pick the most profitable one. If no project
    is affordable, stop early.

Time:  O(n log n + k log n) — heapify once, then k heap pops
Space: O(n) — both heaps hold at most n projects
"""

from collections import defaultdict
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        maxCapital = []
        minCapital = [(c, p)for p, c in zip(profits, capital)]
        heapq.heapify(minCapital)
        heapq.heapify(maxCapital)
        for ct in range(k-1, -1, -1):
            i = 0
            while minCapital and minCapital[0][0] <= w:
                heapq.heappush(maxCapital,[-minCapital[i][1], minCapital[i][0]])
                heapq.heappop(minCapital)
            if maxCapital:
                w += -maxCapital[0][0]
                heapq.heappop(maxCapital)

        return w


if __name__ == '__main__':
    S = Solution()
    k = 2
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]
    print("Output: {}".format(S.findMaximizedCapital(k, w, profits, capital)))
    k = 3
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 2]
    print("Output: {}".format(S.findMaximizedCapital(k, w, profits, capital)))
    k = 2
    w = 0
    profits = [1,2,3]
    capital = [0,1,1]
    print("Output: {}".format(S.findMaximizedCapital(k, w, profits, capital)))

