"""
Valid Sudoku — LeetCode 36 | Arrays & Hashing

Logic:
    Maintain three sets of sets: one per row, one per column, one per 3x3 box.
    For each non-empty cell, check if the value is already in the relevant row,
    column, or box set. If yes, the board is invalid. Otherwise add it to all three.
    Box index is (r // 3, c // 3).

Time:  O(81) = O(1) — fixed 9x9 board, constant iterations
Space: O(81) = O(1) — bounded by board size
"""

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board):
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                else:
                    if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r //3, c //3)]:
                        return False
                    else:
                        rows[r].add(board[r][c])
                        cols[c].add(board[r][c])
                        squares[(r //3),(c //3)].add(board[r][c])

        return True

if __name__ == '__main__':

    board = \
    [["1", "2", ".", ".", "3", ".", ".", ".", "."],
     ["4", ".", ".", "5", ".", ".", ".", ".", "."],
     [".", "9", "1", ".", ".", ".", ".", ".", "3"],
     ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
     [".", ".", ".", "8", ".", "3", ".", ".", "5"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", ".", ".", ".", ".", ".", "2", ".", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "8"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    s1 = Solution()
    print("The given input is a valid Sudoku :\t{}".format("True" if (s1.isValidSudoku(board)) else "False"))

    board =\
    [["1", "2", ".", ".", "3", ".", ".", ".", "."],
     ["4", ".", ".", "5", ".", ".", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", ".", "3"],
     ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
     [".", ".", ".", "8", ".", "3", ".", ".", "5"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", ".", ".", ".", ".", ".", "2", ".", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "8"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    s2 = Solution()
    print("The given input is a valid Sudoku :\t{}".format("True" if (s2.isValidSudoku(board)) else "False"))
