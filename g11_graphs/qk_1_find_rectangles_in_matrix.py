"""
Find Rectangles (Zero Regions) in a Matrix — Karat | Graphs / Matrix DFS

Pattern: Graphs — flood fill / connected component detection
  Scan the matrix for cells with value 0 (top-left corners of zero regions).
  From each unvisited 0, expand right and down to find the bottom-right corner
  of the rectangle. Mark visited cells to avoid double-counting.
  Return list of [top_row, top_col, bot_row, bot_col] for each rectangle.

  Cleaner approach: BFS/DFS flood fill from each unvisited 0 to find full region.

Time:  O(m * n) — each cell visited at most once
Space: O(m * n) — visited marking
"""


def find_rectangles(matrix):
    if not matrix:
        return []
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    result = []

    def get_bounds(r, c):
        bot_r, bot_c = r, c
        while bot_r + 1 < rows and matrix[bot_r + 1][c] == 0:
            bot_r += 1
        while bot_c + 1 < cols and matrix[r][bot_c + 1] == 0:
            bot_c += 1
        return bot_r, bot_c

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0 and not visited[r][c]:
                bot_r, bot_c = get_bounds(r, c)
                result.append([r, c, bot_r, bot_c])
                for dr in range(r, bot_r + 1):
                    for dc in range(c, bot_c + 1):
                        visited[dr][dc] = True

    return result


if __name__ == "__main__":
    matrix = [
        [1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1],
        [1,1,1,0,0,0,1],
        [1,0,1,0,0,0,1],
        [1,0,1,1,1,1,1],
        [1,0,1,0,0,0,0],
        [1,1,1,0,0,0,1],
        [1,1,1,1,1,1,1],
    ]
    for rect in find_rectangles(matrix):
        print(rect)
    # [2,3,3,5], [3,1,5,1], [5,3,6,5]
