"""
Generate Parentheses — LeetCode 22 | Backtracking

Logic:
    Backtrack with two counters: openC (open brackets placed) and closedC (closed placed).
    Add '(' if openC < n. Add ')' if closedC < openC (more closed than open would be invalid).
    Base case: openC == closedC == n → valid combination, add to results.
    Uses a shared stack (list) for efficient string building.

Time:  O(4^n / √n) — the nth Catalan number of valid combinations
Space: O(n) — recursion depth and stack size
"""

class Solution:
    def generateParenthesis(self, n: int):
        res = []
        stack = []

        def backtrack(openC, closedC):
            print(stack)
            if openC == closedC == n:
                res.append("".join(stack))

            if openC < n:
                stack.append('(')
                backtrack(openC+1, closedC)
                stack.pop()

            if closedC < openC:
                stack.append(')')
                backtrack(openC, closedC+1)
                stack.pop()

        backtrack(0,0)
        print(len(res))
        return res

if __name__ == '__main__':
    S1 = Solution()
    n = 3
    print(S1.generateParenthesis(n))

