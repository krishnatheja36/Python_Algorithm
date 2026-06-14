"""
Permutation In String — LeetCode 567 | Sliding Window

Logic:
    Slide a fixed-size window of length len(s1) over s2.
    At each position, rebuild the Counter for the current window and compare to
    Counter(s1). A match means a permutation of s1 starts at that position.

    Optimized approach (not implemented): maintain a single counter and update it
    incrementally (add new char, remove old char) → O(n2) total instead of O(n1 * n2).

Time:  O(n1 * n2) — rebuilding Counter per window step
Space: O(1) — counters bounded by alphabet size (26)
"""

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Fixed-size sliding window of length n1 over s2. At each position, rebuild
        a Counter for the current window and compare it against the Counter for s1.
        A match means s2 contains a permutation of s1 starting at that position.

        Note: rebuilding Counter each step is O(n1) per iteration; an incremental
        update (add new char, remove old char) would reduce this to O(n2) overall.

        Time: O(n1 * n2) — O(n2 - n1) window positions, each rebuilding Counter in O(n1)
        Space: O(1) — counters hold at most 26 keys (lowercase alphabet)
        """
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        c1, c2 = Counter(s1), Counter(s2[0:n1])

        if c1 == c2:
            return True

        for r in range (1, n2-n1+1):
            c2 = Counter(s2[r:n1+r])
            if c1 == c2:
                return True
        return False



if __name__ == '__main__':
    S1 = Solution()
    s1, s2 = "abc", "lecabee"
    print(S1.checkInclusion(s1, s2))