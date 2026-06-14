"""
Unique Paths — LeetCode 62 | 2-D Dynamic Programming

Logic (1D rolling array):
    Paths to any cell = paths from above + paths from the left.
    Initialize a 1D row of 1s (bottom row). For each subsequent row (m-1 times),
    build a new row where newRow[j] = newRow[j+1] + row[j] (scan right to left).
    After m-1 iterations, row[0] holds the answer.

Time:  O(m * n)
Space: O(n) — only one row stored at a time
"""

class Solution:
    def uniquePath(self, m:int, n:int) -> int:
        row = [1] * n
        for i in range(m-1):
            newRow = [1] *n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        
        return row[0]

if __name__ == "__main__":
    S = Solution()
    m = [3, 3]
    n = [7, 2]
    for i, j in zip(m, n):
        print(f"Unique paths for {'i'} and '{j} : {S.uniquePath(i, j)}")