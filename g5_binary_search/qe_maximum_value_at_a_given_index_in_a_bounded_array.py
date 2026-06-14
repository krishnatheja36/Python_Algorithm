"""
Maximum Value at a Given Index in a Bounded Array — LeetCode 1802

Logic:
    Binary search on the candidate peak value (mid) at the given index.
    For each candidate, calculate the minimum possible array sum using the
    arithmetic-series formula: elements rise linearly toward the peak and
    fall away symmetrically on each side (floored at 1). If the sum fits
    within maxSum, the candidate is feasible — search higher; otherwise lower.

Time:  O(log(maxSum)) — binary search on the peak value range
Space: O(1) — only pointer and accumulator variables used
"""

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Maximum Value at a Given Index in a Bounded Array
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Statement:
# Given three positive integers, n, index, and maxSum, output the nums[index] by constructing an array of nums with the length of n, which satisfies the following conditions:
# •	The length of the array nums is equal to n.
# •	Each element nums[i] is a positive integer, where 11≤≤i <<n.
# •	The absolute difference between two consecutive elements, nums[i] and nums[i+1], is at most 11.
# •	The sum of all elements in nums does not exceed maxSum.
# •	The element at nums[index] contains the maximum value.
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Constraints:
# •	11≤≤n ≤≤maxSum ≤≤109109
# •	00≤≤index <<n
# --------------------------------------------------------------------------------------------------------------------------------------------------------


class Solution:
    def calculate_sum(self, index, mid, n):
        count = 0
        
        if mid > index:
            count += (mid + mid - index) * (index + 1) // 2
        else:
            count += (mid + 1) * mid // 2 + index - mid + 1
        
        if mid >= n - index:
            count += (mid + mid - n + 1 + index) * (n - index) // 2
        else:
            count += (mid + 1) * mid // 2 + n - index - mid
        
        return count - mid

    # Function to calculate the max mid
    def max_value(self, n, index, maxSum):
        left, right = 1, maxSum

        while left < right:
            mid = (left + right + 1) // 2

            if self.calculate_sum(index, mid, n) <= maxSum:
                left = mid 
            else:
                right = mid - 1  

        return left

# Driver code
if __name__ == "__main__":
    S = Solution()
    
    input_list = [
    (6, 3, 18),
    (4, 2, 6),
    (3, 0, 3),
    (5, 3, 15),
    (7, 4, 20)]
    
    print("-" * 100, "\nSolution:\n", "-" * 100, sep="")
    for i, (n, index, maxSum) in enumerate(input_list):
        result = S.max_value(n, index, maxSum)
        print(f"{i + 1}.\tInput: n = {n}, index = {index}, maxSum = {maxSum}")
        print(f"\tMaximum mid at index {index}: {result}")
        print('-' * 100)
