"""
Kth Largest Element In An Array — LeetCode 215 | Heap / Priority Queue

Logic:
    Push all elements into a min-heap, keeping its size at most k.
    When the heap exceeds k, pop the smallest. At the end, heap[0] is the kth largest.
    Alternative: QuickSelect achieves O(n) average time.

Time:  O(n log k) — n elements, each heap operation O(log k)
Space: O(k) — heap
"""

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]

if __name__ == "__main__":
    nums = [2,3,1,5,4]
    k = 2
    S = Solution()
    print(S.findKthLargest(nums, k))
