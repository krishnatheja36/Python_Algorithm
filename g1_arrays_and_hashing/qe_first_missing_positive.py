"""
First Missing Positive — LeetCode 41
https://leetcode.com/problems/first-missing-positive/description/

Logic:
    Filter out non-positive numbers. For each remaining number, negate the value
    at index abs(n)-1 to mark that number as "seen". Finally, scan left to right:
    the first index with a positive value means index+1 is missing.
    If all are negative, return len(nums)+1.

Time:  O(n) — two passes through the filtered array
Space: O(1) — marking is done in-place on the filtered list
"""

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums = [n for n in nums if n > 0]
        for n in nums:
            idx = abs(n) - 1
            if idx < len(nums) and nums[idx] > 0:
                nums[idx] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1

        return len(nums) + 1


if __name__ == '__main__':
    S = Solution()
    print("-" * 100, "\nSolution:\n", "-" * 100, sep="")
    
    input_array = [[1, 2, 3, 4], [-1, 3, 5, 7, 1], [1, 5, 4, 3, 2], [-1 , 0, 2, 1, 4], [1,4,3]]
    x = 1
    for i in range(len(input_array)):
        print(x, ".\tThe first missing positive integer in the list ", input_array[i], " is: ", sep = "")
        print("\t" + str(S.firstMissingPositive(input_array[i])))
        print("-" * 100)
        x = x + 1