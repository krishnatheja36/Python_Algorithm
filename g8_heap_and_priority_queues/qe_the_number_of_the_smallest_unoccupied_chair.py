"""
The Number of the Smallest Unoccupied Chair — LeetCode 1942
https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

Logic:
    Sort friends by arrival time. Maintain two min-heaps: used_chairs (leave_time,
    chair_number) and available_chairs (chair_number). For each arriving friend,
    free all chairs whose occupant has left (leave_time ≤ arrival). Assign the
    smallest available chair. Return the chair when the target friend arrives.

Time:  O(n log n) — sorting plus n heap operations
Space: O(n) — both heaps hold at most n entries
"""

import heapq

class Solution:

    def smallest_chair(self, times, target_friend):
        times = [(t[0], t[1], i) for i,t in enumerate(times)]
        times.sort()

        used_chairs = []
        available_chairs = [i for i in range(len(times))]

        for a, l, i in times:
            while used_chairs and used_chairs[0][0] <=a:
                _, chair = heapq.heappop(used_chairs)
                heapq.heappush(available_chairs, chair)

            chair  = heapq.heappop(available_chairs)
            heapq.heappush(used_chairs, [l,chair])

            if i == target_friend:
                return chair

# Driver code
if __name__ == "__main__":
    S = Solution()
    test_cases = [
        ([[3, 6], [1, 6], [4, 5], [2, 4], [5, 7]], 4),
        ([[3, 5], [2, 6], [1, 7]], 0),
        ([[5, 10], [2, 3], [3, 8], [1, 6]], 3),
        ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
        ([[1, 10], [2, 3], [3, 4], [4, 5], [5, 6]], 4)
    ]
    
    for i, (times, target_friend) in enumerate(test_cases):
        result = S.smallest_chair(times, target_friend)
        print(f"{i+1}.\t Times: {times} \n\t Target friend: {target_friend} \n\t Target friend time :{times[target_friend]} \n\n\t Chair number: {result}")
        print("-" * 100)

