"""
House Robber II — LeetCode 213 | 1-D Dynamic Programming

Logic:
    Houses are arranged in a circle — first and last can't both be robbed.
    Reduce to two linear House Robber problems:
      a) Rob houses [1:] (exclude first)
      b) Rob houses [:-1] (exclude last)
    Take the max of those two results (and nums[0] alone as a base case).

Time:  O(n) — two linear passes
Space: O(1) — two rolling variables per pass (slices create O(n) copies though)
"""

class Solution:
    def rob(self, nums: list[int]) ->int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

# DFS solution
    def rob2(self, nums: list[int]) ->int:
        return max(nums[0], self.helper2(nums[1:]), self.helper2(nums[:-1]))
        
    def helper2(self, nums: list[int]) ->int:
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
    nums = [[2,3,2],[1,2,3,1],[1,2,3]]
    print(nums)
    for n in nums:
        print(f"Max amout robbed in {n} : {S.rob(n)}")
        print(f"Max amout robbed in {n} : {S.rob2(n)}")
