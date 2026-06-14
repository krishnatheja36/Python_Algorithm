"""
N Queens — LeetCode 51 | Backtracking

Logic:
    Place one queen per row. Track three forbidden sets:
      - col: columns already occupied
      - posDiag: (r + c) — positive diagonals (top-left to bottom-right)
      - negDiag: (r - c) — negative diagonals (top-right to bottom-left)
    For each row, try every column not in any forbidden set. Place, recurse to next row,
    then remove (backtrack). When r == n, record a copy of the board.

Time:  O(n!) — pruning reduces actual work significantly
Space: O(n²) — board storage + three O(n) constraint sets
"""

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = 'Q'

                backtrack(r +1)

                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = '.'

        backtrack(0)
        return res
if __name__ == '__main__':
    n = 4
    S = Solution()
    print("Output : {}".format(S.solveNQueens(n)))