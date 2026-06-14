"""
Longest Consecutive Sequence — LeetCode 128 | Arrays & Hashing

Logic:
    Build a hash set of all numbers. For each number that has no (num - 1)
    neighbor (i.e., it's the start of a sequence), count forward how many
    consecutive integers exist in the set. Track the longest run seen.
    Skipping non-starts ensures each sequence is counted only once → O(n).

Time:  O(n) — each number is visited at most twice (once as start check, once in run)
Space: O(n) — hash set
"""

class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if (num-1) not in numSet:
                length = 1
                while num + length in numSet:
                    length +=1
                longest = max(length, longest)
        return longest

if __name__ == '__main__':
    nums = [2, 20, 4, 10, 3, 4, 5]
    sol1 = Solution()
    print("Longest consecutive sequence length in {} is : {}".format(nums, sol1.longestConsecutive(nums)))
    nums = [0, 3, 2, 5, 4, 6, 1, 1]
    sol2 = Solution()
    print("Longest consecutive sequence length in {} is : {}".format(nums, sol2.longestConsecutive(nums)))
