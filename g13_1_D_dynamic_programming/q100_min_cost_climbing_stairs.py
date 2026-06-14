"""
Min Cost Climbing Stairs — LeetCode 746 | 1-D Dynamic Programming

Two approaches:

  1. minCostClimbingStairs — top-down DFS (no memoization):
       cost[i] + min(dfs(i+1), dfs(i+2)), called from both index 0 and 1.
       Recomputes subproblems. Time: O(2^n) | Space: O(n) call stack

  2. minCostClimbingStairsndfs — bottom-up DP (in-place):
       Append a 0 cost at the top. Walk backward: cost[i] += min(cost[i+1], cost[i+2]).
       After the loop, the answer is min(cost[0], cost[1]).
       Time: O(n) | Space: O(1) — modifies input in-place
"""

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        def dfs(i):
            if i >=len(cost):
                return 0
            return cost[i] + min(dfs(i+1), dfs(i+2))
        return min(dfs(0), dfs(1))

    def minCostClimbingStairsndfs(self, cost:list[int]) -> int:
        cost.append(0)

        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])


        return min(cost[0], cost[1])
if __name__ == "__main__":
    S = Solution()
    cost = [[1,2,3], [1,2,1,2,1,1,1]]
    for c in cost:
        print("Cost to climb stairs {} is {}".format(c, S.minCostClimbingStairs(c)))
    for c in cost:
        print("Cost to climb stairs {} is {}".format(c, S.minCostClimbingStairsndfs(c)))
