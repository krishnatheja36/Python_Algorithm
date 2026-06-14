"""
Flood Fill — Karat / LeetCode 733 | Backtracking / DFS

Pattern: DFS (backtracking on a grid)
  Start at (sr, sc). Record the original color v = image[sr][sc].
  DFS in all 4 directions: if a cell matches v and hasn't been visited,
  paint it with the new color and recurse. A visited set prevents cycles
  when the new color equals the original color.

Time:  O(m * n) — each cell visited at most once
Space: O(m * n) — visited set + recursion stack
"""


class Solution:
    def flood_fill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        rows, cols = len(image), len(image[0])
        original = image[sr][sc]
        visited = set()

        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols
                    or image[r][c] != original or (r, c) in visited):
                return
            image[r][c] = color
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image


if __name__ == '__main__':
    S = Solution()
    print(S.flood_fill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
    # [[2,2,2],[2,2,0],[2,0,1]]
