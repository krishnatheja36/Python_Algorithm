"""
Target Sum — LeetCode 494 | 2-D Dynamic Programming

Logic (top-down DFS + memoization):
    At each index i, assign either + or - to nums[i] and recurse.
    State: (i, cur_sum). Base: i == len(nums) → 1 if cur_sum == target else 0.
    Memoize (i, cur_sum) to avoid recomputing overlapping subproblems.

Time:  O(n * S) — n = len(nums), S = range of possible sums (2 * sum(nums) + 1)
Space: O(n * S) — memoization cache
"""

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp = {}

        def backtrack(i, cur_sum):
            if (i, cur_sum) in dp:
                return dp[(i, cur_sum)]
            if i == len(nums):
                return 1 if cur_sum == target else 0            
            dp[(i, cur_sum)] = backtrack(i+1, cur_sum + nums[i]) + backtrack(i+1, cur_sum - nums[i])
            return dp[(i, cur_sum)]    
        return backtrack(0, 0)


if __name__ == "__main__":
    S = Solution()
    nums = [2,2,2]
    target = 2
    print(f"Number of ways to get the target sum `{target}` from {nums} : {S.findTargetSumWays(nums, target)}")


