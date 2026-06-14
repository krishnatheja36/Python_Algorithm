"""
Valid Anagram — LeetCode 242 | Arrays & Hashing

Logic:
    Use Counter to build character-frequency maps for both strings.
    Two strings are anagrams if and only if their frequency maps are equal.
    Handles unicode characters naturally; Counter comparison is O(n).

Time:  O(n) — building and comparing two Counters
Space: O(n) — at most n distinct characters across both counters
"""

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    S = Solution()
    print(f"'{s} and {t} are anagrams: {S.isAnagram(s, t)}")

