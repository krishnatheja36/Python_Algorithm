"""
Best Time to Buy and Sell Stock With Cooldown — LeetCode 309 | 2-D Dynamic Programming

Logic (top-down DFS + memoization):
    State: (index, buying) — whether we're looking to buy or sell at day i.
    If buying:  option to buy (transition to not-buying at i+1, subtract price)
                or cooldown (stay buying at i+1).
    If selling: option to sell (transition to buying at i+2 due to cooldown, add price)
                or cooldown (stay selling at i+1).
    Memoize (i, buying) pairs to avoid recomputation.

Time:  O(n) — 2n unique states (n days × 2 buy/sell states)
Space: O(n) — memoization cache + call stack
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            
            return dp[(i, buying)]
        
        return dfs(0, True)


if __name__ == '__main__':
    S = Solution()
    prices = [[1,3,4,0,4], [1] ]
    for p in prices:
        print(f"Max profit for the given prices {p}: {S.maxProfit(p)}")