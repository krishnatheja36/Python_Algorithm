"""
Diet Plan Performance — LeetCode 1176
https://leetcode.com/problems/diet-plan-performance/description/

Logic:
    Fixed-size sliding window of length k. Compute the initial window sum for the
    first k elements, then slide by subtracting the outgoing element and adding the
    incoming one. After each step compare the sum against lower and upper bounds
    and adjust the points total.

Time:  O(n) — single pass after the initial window setup
Space: O(1) — only a constant number of variables maintained
"""

class Soultion:

    def diet_plan_performance(self, calories, k, lower, upper):
        points = 0
        current_sum = sum(calories[:k])

        if current_sum < lower:
            points -= 1
        elif current_sum > upper:
            points += 1

        for i in range(k, len(calories)):
            current_sum = current_sum - calories[i - k] + calories[i]
            if current_sum < lower:
                points -= 1
            elif current_sum > upper:
                points += 1

        return points

if __name__ == "__main__":
    S = Solution()
    test_cases = [
        ([3, 5, 8, 2, 6], 2, 7, 10),       # Test Case 1: Mixed performance
        ([1, 1, 1, 1, 1], 2, 5, 10),      # Test Case 2: All sums below the lower limit
        ([10, 12, 15, 20, 25], 3, 10, 30), # Test Case 3: All sums above the upper limit
        ([5, 10, 15, 20, 25, 30], 3, 20, 40), # Test Case 4: Mix of poor, normal, and good performances
        ([3, 8, 7, 4, 5, 6], 2, 7, 10)     # Test Case 5: Sliding window with variable performance
    ]

    
    for i, (calories, k, lower, upper) in enumerate(test_cases, 1):
        print(f"Test Case {i}:")
        print(f"\tcalories = {calories}")
        print(f"\tk = {k}")
        print(f"\tlower = {lower}")
        print(f"\tupper = {upper}")
        result = S.diet_plan_performance(calories, k, lower, upper)
        print(f"\n\tpoints = {result}")
        print("-"*100)

