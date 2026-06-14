"""
Max Area of Island — LeetCode 695 | Graphs

Logic:
    DFS from every unvisited land cell (value 1). Each DFS call returns 1 +
    the area of all 4-directionally connected unvisited land cells.
    Out-of-bounds, water (0), and already-visited cells return 0.
    Track the maximum area returned across all DFS calls.

Time:  O(m * n) — each cell visited at most once
Space: O(m * n) — visited set + recursion stack
"""

import collections

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def dfs(r, c):
            if r <0 or r == rows or c <0 or c == cols or grid[r][c] == 0 or (r,c) in visit:
                return 0
            else:
                visit.add((r,c))
                return (1 + dfs(r + 1,c) + dfs(r -1 ,c) + dfs(r,c+1) + dfs(r,c-1))

        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r,c))
        return area
        

if __name__ == "__main__":
    grids = [
    [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ],
    [
        [0,0,0,0,0,0,0,0]
    ]
    ]

    S = Solution()
    for grid in grids:
        print("-"*50)
        print(f"Max area of isalnds in the given ip {grid} is: {S.maxAreaOfIsland(grid)}")
    print("-"*50)