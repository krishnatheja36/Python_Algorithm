"""
Split Array Largest Sum — LeetCode 410
https://leetcode.com/problems/split-array-largest-sum/description/

Logic:
    Binary search on the answer. The search range is [max(nums), sum(nums)].
    For each candidate maximum subarray sum (mid), greedily check whether the
    array can be split into at most k subarrays each with sum ≤ mid. If feasible,
    search lower; otherwise search higher.

Time:  O(n log(sum)) — binary search with O(n) feasibility check each iteration
Space: O(1) — only pointer and counter variables used
"""

class Solution:

    def can_split(self, nums, k, mid):
        subarrays = 1
        current_sum = 0

        for num in nums:
            if current_sum + num > mid:
                subarrays += 1
                current_sum = num
                
                if subarrays > k:
                    return False
            else:
                current_sum += num
        
        return True


    def split_array(self, nums, k):
        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) // 2
            
            if self.can_split(nums, k, mid):
                right = mid
            else:
                left = mid + 1
        
        return left


if __name__ == "__main__":
    S = Solution()
    print("-" * 100, "\nSolution:\n", "-" * 100, sep="")
    split = [[3, 4, 6, 3],
              [2, 7, 8, 9, 2, 1, 4],
              [12, 53, 43, 67, 35],
              [4, 6, 4, 6, 4, 6],
              [11, 11, 11, 11, 11]]
    k = [3, 6, 5, 4, 2]
    
    for i in range(len(split)):
        print(i+1, ".\tInput Array:", split[i])
        print("\tk:", k[i])
        print("\n\tLargest minimized sum:", S.split_array(split[i], k[i]))
        print("-" * 100)   
