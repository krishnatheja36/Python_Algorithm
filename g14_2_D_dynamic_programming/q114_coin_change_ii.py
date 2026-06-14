"""
Coin Change II — LeetCode 518 | 2-D Dynamic Programming

Logic (top-down DFS + memoization, unbounded knapsack):
    State: (coin_index i, current_amount a).
    At each state: use coin[i] again (dfs(i, a + coins[i])) OR skip to next coin (dfs(i+1, a)).
    Base cases: a == amount → 1 way; a > amount or i == len(coins) → 0 ways.
    Memoizing (i, a) collapses the exponential tree.

Time:  O(n * amount) — n coins × amount values per coin
Space: O(n * amount) — memoization cache
"""

class Solution:
    def coinchange(self, amount:int, coins:list) -> int:
        cache = {}

        def dfs(i, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in cache:
                return cache[(i, a)]          
            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i+1, a)
            return cache[(i, a)]
        
        return dfs(0,0)


if __name__ == "__main__":
    S = Solution()
    amount = [4, 7]
    coins = [[1,2,3], [2,4]]
    for a, c in zip(amount, coins):
        print(f"For amount `{a}` in coins {c} possible change is: {S.coinchange(a, c)}")
