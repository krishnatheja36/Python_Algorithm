"""
Find Right Interval — LeetCode 436
https://leetcode.com/problems/find-right-interval/description/

Logic:
    Build two min-heaps: one sorted by interval start points, one by end points.
    Process intervals in order of their end time. For each end point, pop any start
    points from the start heap that are smaller than the current end (they cannot be
    the right interval). The top of the start heap (if any) is the right interval.

Time:  O(n log n) — two heapify operations and n heap pops
Space: O(n) — both heaps hold at most n intervals
"""

import heapq

class Solution:

    def find_right_interval(self, intervals):
        result = [-1] * len(intervals)
        
        start_heap = []
        end_heap = []
        
        for i, interval in enumerate(intervals):
            heapq.heappush(start_heap, (interval[0], i))
            heapq.heappush(end_heap, (interval[1], i))
        
        while end_heap:
            value, index = heapq.heappop(end_heap)
            
            while start_heap and start_heap[0][0] < value:
                heapq.heappop(start_heap)
            
            if start_heap:
                result[index] = start_heap[0][1]
        
        return result

if __name__ == "__main__":
    S = Solution()

    test_cases = [
        [[1, 2]],
        [[3, 4], [2, 3], [1, 2]],
        [[1, 4], [2, 3], [3, 4]],
        [[5, 6], [1, 2], [3, 4]],
        [[1, 3], [2, 4], [3, 5], [4, 6]],
    ]

    for i, test_case in enumerate(test_cases):
        print(i + 1, "\tintervals:", test_case)
        result = S.find_right_interval(test_case)
        print("\n\tOutput:", result)
        print("-" * 100)

