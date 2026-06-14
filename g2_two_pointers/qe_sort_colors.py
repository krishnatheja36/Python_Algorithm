"""
Sort Colors — LeetCode 75
https://leetcode.com/problems/sort-colors/description/

Logic:
    Dutch National Flag algorithm with three pointers: l (left boundary for 0s),
    i (current element), r (right boundary for 2s). If nums[i] == 0 swap with l
    and advance both. If nums[i] == 2 swap with r and retreat r (don't advance i).
    If nums[i] == 1 advance i only.

Time:  O(n) — single pass through the array
Space: O(1) — sorting is done in-place with three pointer variables
"""

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        l, i, r = 0, 0, len(nums)-1
        while i <= r:
            print("Steps :", nums)
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l +=1
            elif nums[i] ==2:
                nums[r], nums[i] = nums[i], nums[r]
                r -=1
                i -=1
            i +=1

        return nums

if __name__ == '__main__':
    S = Solution()
    inputs = [[0, 1, 0], [1, 1, 0, 2], [2, 1, 1, 0, 0], [2, 2, 2, 0, 1, 0], [2, 1, 1, 0, 1, 0, 2]]

    for i in range(len(inputs)):
        colors=inputs[i]
        print(i + 1, ".\tcolors:", colors)
        S.sortColors(colors)
        print("\n\tThe sorted array is:", colors)
        print("-" * 100)
