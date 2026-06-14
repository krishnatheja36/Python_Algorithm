"""
Combinations — LeetCode 77 | Backtracking

Logic:
    Uses Python's itertools.combinations to generate all k-sized subsets of [1..n].
    Also demonstrates itertools.permutations for comparison.

Time:  O(C(n,k) * k) — generating each combination takes O(k) to copy
Space: O(C(n,k) * k) — all combinations stored in memory
"""

from itertools import combinations, permutations
n = 4
k = 2
nums =  [i+1 for i in range(n)]
print(list(combinations(nums, k)))
print(list(permutations(nums, k)))