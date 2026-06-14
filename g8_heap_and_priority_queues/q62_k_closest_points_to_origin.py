"""
K Closest Points to Origin — LeetCode 973 | Heap / Priority Queue

Logic:
    Use a max-heap of size k (simulated with negated distances).
    For each point, push (-distance², x, y). If the heap grows beyond k, pop the
    farthest point. At the end the heap contains the k closest points.

Time:  O(n log k) — each push/pop is O(log k)
Space: O(k) — heap size
"""

import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        maxHeap = []
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        return res


if __name__ == "__main__":
    points = [[0,2],[2,0],[2,2]]
    k = 2
    S = Solution()
    print(S.kClosest(points,k))
