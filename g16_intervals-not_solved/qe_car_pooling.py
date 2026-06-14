"""
Car Pooling — LeetCode 1094
https://leetcode.com/problems/car-pooling/description/

Logic:
    Sort trips by start location. Use a min-heap keyed by drop-off location to
    track passengers currently in the car. For each new trip, pop all passengers
    who have been dropped off (drop-off ≤ current start). Add the new passengers
    and check if total exceeds capacity.

Time:  O(n log n) — sorting plus n heap operations
Space: O(n) — heap can hold all n trips in the worst case
"""

# Function under test

import heapq


class Solution:

    def carPooling(self, trips, capacity):
        trips.sort(key = lambda x: x[1])
        min_heap =[]
        num_pass = 0
        for new_pass, start, end in trips:
            while min_heap and min_heap[0][0] <= start:
                num_pass -= min_heap[0][1]
                heapq.heappop(min_heap)

            num_pass += new_pass
            if num_pass > capacity:
                return False
            else:
                heapq.heappush(min_heap,[end, num_pass])
        
        return True

# Driver code
if __name__ == "__main__":
    S = Solution()
    test_cases = [
        ([[2, 1, 5], [3, 3, 7]], 4),
        ([[2, 1, 5], [3, 3, 7]], 5),
        ([[3, 2, 6], [1, 4, 7], [2, 5, 8]], 5),
        ([[1, 0, 4], [2, 2, 6], [3, 5, 8]], 6),
        ([[4, 1, 5], [1, 3, 7], [2, 6, 8]], 5)
    ]

    for i, (trips, capacity) in enumerate(test_cases, start=1):
        print(f"{i}.\tInput: trips = {trips}, capacity = {capacity}")
        result = S.carPooling(trips, capacity)
        print(f"\tCan complete all trips? {result}")
        print("-" * 100)
