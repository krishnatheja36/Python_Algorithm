"""
Longest Common Subsequence — LeetCode 1143 | 2-D Dynamic Programming

Logic (bottom-up 2D DP):
    dp[i][j] = LCS length for text1[i:] and text2[j:].
    If text1[i] == text2[j]: dp[i][j] = 1 + dp[i+1][j+1].
    Otherwise: dp[i][j] = max(dp[i+1][j], dp[i][j+1]) (skip one char from either string).
    Fill from bottom-right to top-left. Answer is dp[0][0].

Time:  O(m * n) — m = len(text1), n = len(text2)
Space: O(m * n) — 2D dp table (can be reduced to O(n) with rolling rows)
"""

class Solution:
    def longestcommonsubsequence(self, text1:str, text2:str) -> int:
        dp = [[0 for j in range(len(text2) +1)] for i in range(len(text1) +1)]
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]

if __name__ == "__main__":
    S = Solution()
    text1 = ["cat", "abcd", "abcd"]
    text2 = ["crabt", "abcd", "efgh"]
    for i, j in zip(text1, text2):
        print(f"longestcommonsubsequence for '{i}' and '{j} : {S.longestcommonsubsequence(i, j)}")