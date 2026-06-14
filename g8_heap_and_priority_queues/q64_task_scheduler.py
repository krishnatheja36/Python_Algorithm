"""
Task Scheduler — LeetCode 621 | Heap / Priority Queue

Logic:
    Use a max-heap (negated counts) to always run the most frequent available task.
    A cooldown queue holds tasks that are on cooldown as [remaining_count, ready_time].
    Each time unit: pop from heap (if available), decrement count, push to cooldown queue.
    When a task's cooldown expires (ready_time == current_time), push it back to heap.
    Count total time units including idle cycles.

Time:  O(n log n) — n tasks, heap operations per unit of time
Space: O(n)
"""

import heapq

from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque()
        while maxHeap or q:
            time +=1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time +n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return time
                
if __name__ == "__main__":
    tasks = ["X","X","Y","Y"]
    n = 2
    S = Solution()    
    print(S.leastInterval(tasks, n))
