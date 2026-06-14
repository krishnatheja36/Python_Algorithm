"""
Find K Closest Elements — LeetCode 658
https://leetcode.com/problems/find-k-closest-elements/description/

Logic:
    Binary search to find the insertion point of the target, then expand a window
    of size k outward. At each step pick the side whose element is closer to target.
    Edge cases: target before first element returns nums[0:k]; target after last
    returns the last k elements.

Time:  O(log n + k) — O(log n) for binary search, O(k) to expand the window
Space: O(1) — only pointer variables used (result is a slice of input)
"""

class Solution:
    def binary_search(self, array, target):

        left = 0
        right = len(array) - 1

        while left <= right:
            mid = (left + right) // 2
            if array[mid] == target:
                return mid
            if array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def find_closest_elements(self, nums, k, target):
        if len(nums) == k:
            return nums

        if target <= nums[0]:
            return nums[0:k]
            
        if target >= nums[-1]:
            return nums[len(nums)-k : len(nums)]

        first_closest = self.binary_search(nums, target)

        window_left = first_closest - 1
        window_right = first_closest
        

        while (window_right - window_left - 1) < k:
            if window_left == -1:
                window_right += 1
                continue

            if window_right == len(nums) or abs(nums[window_left] - target) <= abs(nums[window_right] - target):
                window_left -= 1
            
            else:
                window_right += 1
        return nums[window_left+1 : window_right]

if __name__ == "__main__":
    S = Solution()
    print("-" * 100, "\nSolution:\n", "-" * 100, sep="")
    nums = [
                [1, 2, 3, 5, 6, 7,8],
                [1, 2, 3, 4, 5],
                [1, 2, 4, 5, 6],
                [1, 2, 3, 4, 5, 10]
                ]
    k = [4, 4, 2, 3]
    num = [4, 3, 10, -5]
    for i in range(len(nums)):
        print((i + 1), ".\tThe ", k[i],
              " Closest Elements for the number ", num[i], " in the array ",
              nums[i], " are:", sep="")
        print("\t", S.find_closest_elements(nums[i], k[i], num[i]))
        print("-" * 100)
