"""
Kth Largest Element In a Stream — LeetCode 703 | Heap / Priority Queue

Logic:
    Maintain a min-heap of exactly k elements. The heap's root (heap[0]) is always
    the kth largest seen so far. On each add: push the new value, then if the heap
    exceeds k elements, pop the smallest. Return heap[0].
    Initialization heapifies the input and trims down to k elements.

Time:  O(log k) per add
Space: O(k) — heap size bounded by k
"""

import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

if __name__ == "__main__":
    kthLargest =  KthLargest(3, [1, 2, 3, 3]);
    print(kthLargest.add(3))   # return 3
    print(kthLargest.add(5))   # return 3
    print(kthLargest.add(6))   # return 3
    print(kthLargest.add(7))   # return 5
    print(kthLargest.add(8))   # return 6