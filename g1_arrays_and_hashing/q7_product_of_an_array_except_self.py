"""
Product of Array Except Self — LeetCode 238 | Arrays & Hashing

Logic (implemented — brute force):
    For each position j in the output, multiply all nums[i] where i != j.
    This is O(n^2) — two nested loops.

Optimal approach (not implemented):
    Two passes — prefix pass builds left products, suffix pass multiplies in right products.
    Output[i] = product of all elements to the left * product of all elements to the right.

Time:  O(n^2) — current brute force
Space: O(n)   — output array
Optimal Time:  O(n) | Optimal Space: O(1) excluding output
"""

import math

class Solution:
    def productExceptSelf(self, nums):
        nums_product = [1] *len(nums)
        for i, num in enumerate(nums):
            for j in range(len(nums)):
                if i != j:
                    nums_product [j] = nums_product [j] * nums[i]

        return nums_product

if __name__ == '__main__':
    nums = [-1,0,1,2,3]
    S1 = Solution()
    print(S1.productExceptSelf(nums))