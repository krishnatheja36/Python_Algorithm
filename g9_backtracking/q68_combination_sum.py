"""
Combination Sum — LeetCode 39 | Backtracking

Logic:
    Two DFS variants over the candidates array:
    - non_repeating: at each index n, branch include-then-skip, always advancing
      n+1 in both branches — each candidate used at most once.
    - repeating (LeetCode 39): when including candidates[n], recurse with same n
      (reuse allowed); skip by advancing to n+1. Prunes when running sum > target.

non_repeating  Time: O(2^n * n) — 2^n subsets, O(n) to copy each
               Space: O(n) — recursion depth equals number of candidates
repeating      Time: O(n^(t/m)) — t = target, m = min element; exponential branching
               Space: O(t/m) — max recursion depth is target / min_element
"""

class Solution:
    def combinationSum_non_repeating(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        subset = []

        def dfs(n):
            if sum(subset) == target:
                result.append(subset[:])
                return
            if sum(subset)>target or n==len(candidates):
                return

            subset.append(candidates[n])
            dfs(n+1)
            subset.pop()
            dfs(n+1)

        dfs(0)
        return result

    def combinationSum_repeating(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        subset = []

        def dfs(n):
            if sum(subset) == target:
                result.append(subset[:])
                return
            if sum(subset)>target or n == len(candidates):
                return

            subset.append(candidates[n])
            dfs(n)
            subset.pop()

            dfs(n+1)

        dfs(0)
        return result

if __name__ == "__main__":
    candidates = [2,3,5]
    target = 8
    S = Solution()
    print("Combination Sums: ", S.combinationSum_non_repeating(candidates=candidates, target=target))
    print("Combination Sums: ", S.combinationSum_repeating(candidates=candidates, target=target))
