"""
Search a 2D Matrix — LeetCode 74 | Binary Search

Two approaches:

  1. binarysearch — double binary search:
       First binary search finds the correct row (target between row[0] and row[-1]).
       Second binary search finds the column within that row.
       Time: O(log m + log n) | Space: O(1)

  2. step_searchMatrix — staircase search (top-right corner):
       Start at top-right. If value > target, move left (c -= 1).
       If value < target, move down (r += 1). No backtracking needed.
       Time: O(m + n) | Space: O(1)
"""

class Solution:

    def binarysearch(self, nums: list[int], target: int) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
    
    def step_searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1

        while r < m and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        return False

if __name__ == "__main__":
    S = Solution()
    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target = 13
    print(f"Target '{target}' found in index '{S.binarysearch(matrix, target)}' in {matrix}")
    print(f"Target '{target}' found in index '{S.step_searchMatrix(matrix, target)}' in {matrix}")
