"""
Two Sum II - Input Array Is Sorted — LeetCode 167 | Two Pointers

Logic:
    Array is sorted, so use l and r pointers at both ends.
    If the sum is too small, advance l. If too large, retreat r.
    When the sum equals target, return 1-indexed positions.
    Guaranteed exactly one solution, so no edge case handling needed.

Time:  O(n) — pointers traverse at most n steps combined
Space: O(1) — no extra storage
"""

class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) -1

        while l < r:
            s = numbers[l] + numbers[r]
            if s < target:
                l +=1
            elif s > target:
                r -=1
            else:
                return [l+1, r+1]
        return[]


if __name__ == '__main__':
    numbers = [1, 2, 3, 4]
    target = 3

    s1 = Solution()
    print(s1.twoSum(numbers, target))

