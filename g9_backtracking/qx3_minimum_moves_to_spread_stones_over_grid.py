"""
Minimum Moves to Spread Stones Over Grid — LeetCode 2850
https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/description/

Logic:
    Incomplete implementation. The intended approach: collect cells with 0 stones
    (needs) and cells with excess stones (sources), then try all permutations of
    assigning excess stones to empty cells, tracking Manhattan distance to find
    the minimum total moves.

Time:  O(k!) — k = number of empty cells; brute-force permutations
Space: O(k) — recursion depth
"""

import math
# grid = [[1,1,0],[1,1,1],[1,2,1]]
# print(math.prod(grid[0] + grid[1]  + grid[2]))

class Solution:
    def minimumMoves(self, grid: list[list[int]]) -> int:
        def backtrack(i, j, grid, ct):
            if math.prod(grid[0] + grid[1]  + grid[2]) == 1:
                return 

if __name__ == '__main__':
    S = Solution()
    grid = [[1, 1, 0], [1, 1, 1], [1, 2, 1]]

