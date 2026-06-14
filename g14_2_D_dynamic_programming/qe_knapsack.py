"""
0/1 Knapsack — 2-D Dynamic Programming

Logic:
    Classic 0/1 knapsack. Iterate over each item; for each item scan the capacity
    array right-to-left (to avoid reusing the same item). Update dp[j] =
    max(dp[j], values[i] + dp[j - weights[i]]). The final answer is dp[capacity].

Time:  O(n * capacity) — two nested loops
Space: O(capacity) — single 1D DP array rolled in-place
"""

# ------------------------------------------------------------------------------------------------------------------------------------------------
# 0/1 Knapsack
# ------------------------------------------------------------------------------------------------------------------------------------------------
# Statement:
# You are given nn items whose weights and values are known, as well as a knapsack to carry these items. The knapsack cannot carry more than a certain maximum weight, known as its capacity.
# You need to maximize the total value of the items in your knapsack, while ensuring that the sum of the weights of the selected items does not exceed the capacity of the knapsack.
# If there is no combination of weights whose sum is within the capacity constraint, return 00.
# ------------------------------------------------------------------------------------------------------------------------------------------------
# Notes:
# 1.	An item may not be broken up to fit into the knapsack, i.e., an item either goes into the knapsack in its entirety or not at all.
# 2.	We may not add an item more than once to the knapsack.
# ------------------------------------------------------------------------------------------------------------------------------------------------
# Constraints:
# •	1≤1≤ capacity ≤1000≤1000
# •	1≤1≤ values.length ≤500≤500
# •	weights.length ==== values.length
# •	1≤1≤ values[i] ≤1000≤1000
# •	1≤1≤ weights[i] ≤≤ capacity
# ------------------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def find_max_knapsack_profit(self, capacity, weights, values):
        n = len(weights)
        dp = [0] * (capacity + 1)

        for i in range(n):
            print("\ni : ", i)
            for j in range(capacity, weights[i] - 1, -1):
                print("j : ", j)
                dp[j] = max(dp[j], (values[i] + dp[j - weights[i]] ))
                print(dp)

        return dp[capacity]

# Driver code
if __name__ == "__main__":
    S = Solution()
    capacity = [6, 3, 3, 10, 20]
    weights = [[1, 2, 3, 5],[4],[2],[3, 6, 10, 7, 2], [3, 6, 10, 7, 2, 12, 15, 10, 13, 20]]
    values = [[1, 5, 4, 8],[2], [3], [12, 10, 15, 17,13], [12, 10, 15, 17,13, 12, 30, 15, 18, 20]]
    n = [4, 1, 1, 5, 10]
    
    for i in range(len(values)):
        print(i+1, ". We have a knapsack of capacity ",capacity[i], " and we are given the following list of item values and weights:", sep="")
        print("-"*30, sep="")
        print("{:<10}{:<5}{:<5}".format("Weights", "|", "Values"))
        print("-"*30)
        for j in range(len(values[i])):
            print("{:<10}{:<5}{:<5}".format(weights[i][j], "|", values[i][j]))
        result = S.find_max_knapsack_profit(capacity[i], weights[i], values[i])
        print("\nThe maximum we can earn is: ", result, sep="")
        print("-"*100, "\n", sep="")

