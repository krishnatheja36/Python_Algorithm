"""
Best Time to Buy and Sell Stock — LeetCode 121 | Sliding Window

Logic:
    Single pass: track the minimum price seen so far (best buy day).
    At each price, compute the profit if selling today (price - lowest).
    Update the running maximum profit. No actual window needed — just two scalars.

Time:  O(n) — single pass
Space: O(1)
"""

class Solution:
    def maxProfit(self, prices):
        res = 0
        lowest = prices[0]
        for price in prices:
            lowest = min(price, lowest)
            res = max(res, price -lowest)

        return res

if __name__ == '__main__':
    s1 = Solution()
    prices = [10, 1, 5, 6, 7, 1, 9]
    print("Max profit for prices :{} is :{}".format(prices, s1.maxProfit(prices)))