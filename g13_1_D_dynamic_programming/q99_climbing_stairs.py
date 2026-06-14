"""
Climbing Stairs — LeetCode 70 | 1-D Dynamic Programming

Two approaches:

  1. climbStairsDFS — naive recursion (no memoization):
       At each step, branch into +1 or +2. Exponential recomputation.
       Time: O(2^n) | Space: O(n) call stack

  2. clibStair2 — DP Fibonacci (rolling two variables):
       Number of ways to reach step n = ways(n-1) + ways(n-2).
       Slide two variables forward; no array needed.
       Time: O(n) | Space: O(1)
"""

class Solution:
    def climbStairsDFS(self, n: int) -> int:
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i + 1) + dfs(i + 2)
        return dfs(0)
    
    def clibStair2(self, n:int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            one, two = (one +two), one
        return one

if __name__ == "__main__":
    S = Solution()
    n = [3, 6, 9, 10]
    for ele in n:
        print("climbStairsDFS - Number of unique ways to reach {} is {}".format(ele, S.climbStairsDFS(ele)))
        print("clibStair2 - Number of unique ways to reach {} is {}".format(ele, S.clibStair2(ele)))
        print("-"*50)