"""
Longest Common Continuous Subarray — Karat | Sliding Window

Pattern: Sliding Window (variable, two-sequence variant)
  Fix a start index i in list1. Walk both lists in parallel from i and j=0.
  When elements match extend the run; on mismatch, reset n back to i and
  advance j. Track the longest matching run seen across all start positions.

  Optimal: DP — dp[i][j] = length of common subarray ending at list1[i], list2[j].
  If list1[i] == list2[j]: dp[i][j] = dp[i-1][j-1] + 1, else 0.

Time:  O(n * m) — n = len(list1), m = len(list2)
Space: O(k)     — k = length of result subarray
"""


def longest_common_subarray(list1, list2):
    best = []
    for i in range(len(list1)):
        n, j = i, 0
        while j < len(list2) and n < len(list1):
            if list1[n] == list2[j]:
                if n - i + 1 > len(best):
                    best = list1[i:n + 1]
                n += 1
                j += 1
            else:
                n = i
                j += 1
    return best


if __name__ == "__main__":
    user1 = ["3234.html", "xys.html", "7hsaa.html"]
    user2 = ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"]
    print(longest_common_subarray(user1, user2))   # ["xys.html", "7hsaa.html"]

    user1 = [1, 2, 3, 4, 5]
    user2 = [6, 2, 3, 4, 7]
    print(longest_common_subarray(user1, user2))   # [2, 3, 4]
