"""
Check if Every Row and Column Contains All Numbers — Karat / LeetCode 2133 | Arrays & Hashing

Pattern: Hash Set validation per row and column
  Each row and each column of an n×n matrix must contain every integer from
  1 to n exactly once. Pre-populate a set {1..n} for each row and column.
  As we scan, discard seen values; if a value is already gone, return False.

Time:  O(n²) — visit every cell once
Space: O(n²) — n sets of size n
"""


def check_valid_matrix(matrix):
    n = len(matrix)
    rows = [set(range(1, n + 1)) for _ in range(n)]
    cols = [set(range(1, n + 1)) for _ in range(n)]

    for r in range(n):
        for c in range(n):
            val = matrix[r][c]
            if val not in rows[r] or val not in cols[c]:
                return False
            rows[r].discard(val)
            cols[c].discard(val)
    return True


if __name__ == "__main__":
    print(check_valid_matrix([[1,2,3],[3,1,2],[2,3,1]]))   # True
    print(check_valid_matrix([[1,1,1],[1,2,3],[1,2,3]]))   # False
