"""
House Robber — LeetCode 198 | 1-D Dynamic Programming

Two approaches:

  1. rob — bottom-up DP with two variables:
       At each house: best = max(rob1 + current, rob2).
       rob1 = previous rob2, rob2 = new best. Slide forward.
       Time: O(n) | Space: O(1)

  2. robdfs — top-down DFS with memoization:
       dfs(i) = max(dfs(i+1), nums[i] + dfs(i+2)). Cache with memo array.
       Time: O(n) | Space: O(n) — memo + call stack
"""

class Solution:
    def rob(self, nums: list[int]) ->int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
    
    def robdfs(self, nums: list[int]) ->int:
        memo = [-1] *len(nums)

        def dfs(i):
            # print(f"calling dfs({i})")
            if i>=len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            # print(f"Returning {memo[i]}: from {memo} i:{i}")
            return memo[i]

        return dfs(0)            

if __name__ == "__main__":
    S = Solution()
    nums = [[1,1,3,3], [2,9,8,3,6]]
    for n in nums:
        print(f"Max amout robbed in {nums} : {S.rob(n)}")
        print(f"Max amout robbed in {nums} : {S.robdfs(n)}")