"""
Last Stone Weight — LeetCode 1046 | Heap / Priority Queue

Logic:
    Python only has a min-heap, so negate all stone weights to simulate a max-heap.
    Repeatedly pop the two heaviest stones. If they differ, push back the difference
    (negated). When one stone remains (or none), return its absolute value (or 0).

Time:  O(n log n) — n pop/push operations each O(log n)
Space: O(n) — heap
"""

import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
                print(stones)

        stones.append(0)
        return abs(stones[0])
    

if __name__ == "__main__":
    stones = [2,3,6,2,4]
    S = Solution()
    print(S.lastStoneWeight(stones))