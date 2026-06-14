"""
Number of Islands — LeetCode 200 | Graphs

Logic:
    Scan every cell. When an unvisited '1' is found, launch a BFS to mark all
    connected land cells as visited (flood fill). Each BFS call = one island.
    BFS explores all 4 neighbors; only visits '1' cells not yet in the visited set.

Time:  O(m * n) — each cell visited at most once
Space: O(m * n) — visited set + BFS queue
"""

import collections

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) 
                        and c in range(cols) 
                        and str(grid[r][c]) == "1" 
                        and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if str(grid[r][c]) == '1' and (r, c) not in visit:
                    bfs(r,c)
                    islands +=1
        
        return islands
    
    def numIslandsDFS(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or int(grid[r][c]) != 1:
                return
            
            grid[r][c] = '0'
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if int(grid[r][c]) == 1:
                    count += 1
                    dfs(r, c)    # sink the entire island
        
        return count


if __name__ == "__main__":
    grids = [
    [["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ],
    [["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ],
    [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    ]
    S = Solution()
    for grid in grids:
        print(f"Number of isalnds in the given ip {grid} is: {S.numIslands(grid)}")
        print(f"Number of isalnds in the given ip {grid} is: {S.numIslandsDFS(grid)}")