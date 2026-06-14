"""
Daily Temperatures — LeetCode 739 | Stack (Monotonic)

Logic:
    Maintain a monotonic decreasing stack of (temperature, index) pairs.
    For each day, pop all stack entries with a temperature lower than today's —
    those days finally found a warmer day. Record the gap (i - stackInd) in res.
    Push current day onto the stack. Remaining stack entries have answer 0 (default).

Time:  O(n) — each element pushed and popped at most once
Space: O(n) — stack
"""

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res


if __name__ == "__main__":
    S = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    print("Given temps  : ", temperatures)
    print("Output       : ", S.dailyTemperatures(temperatures))

        
