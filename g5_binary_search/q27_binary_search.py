"""
Binary Search — LeetCode 704 | Binary Search

Logic:
    Standard binary search on a sorted array. Maintain l and r pointers.
    Compute mid as l + (r - l) // 2 (avoids integer overflow vs (l+r)//2).
    If nums[mid] > target, search left half (r = mid - 1).
    If nums[mid] < target, search right half (l = mid + 1).
    Return mid on match, -1 if l > r.

Time:  O(log n) — halve search space each step
Space: O(1)
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # (l + r) // 2 can lead to overflow
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

if __name__ == "__main__":
    S = Solution()
    nums = [-1,0,2,4,6,8]
    target = 4
    print(f"Target '{target}' found in index '{S.search(nums, target)}' in {nums}")
    