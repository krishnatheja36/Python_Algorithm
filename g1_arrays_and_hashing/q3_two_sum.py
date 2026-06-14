"""
Two Sum — LeetCode 1 | Arrays & Hashing

Logic:
    One-pass hashmap. For each number, compute its complement (target - num).
    If the complement already exists in the map, we found the pair — return both indices.
    Otherwise store the current number → index in the map for future lookups.

Time:  O(n) — single pass, O(1) average hashmap lookup
Space: O(n) — hashmap stores up to n elements
"""

class Solution:

    def twoSum(self, nums, target):
        prevMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff],i]
            else:
                prevMap[num] = i


if __name__ == "__main__":
    S = Solution()
    nums = [2,7,11,15]
    target = 9
    print(f"2Sum for target '{target}' in nums {nums} : {S.twoSum(nums, target)}")