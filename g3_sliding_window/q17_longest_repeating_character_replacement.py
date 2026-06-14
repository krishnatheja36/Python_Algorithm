"""
Longest Repeating Character Replacement — LeetCode 424 | Sliding Window

Two approaches:
  1. characterReplacement1 — recomputes max frequency each step via max(map_ct.values())
       Time: O(n * 26) | Space: O(1)

  2. characterReplacement2 — tracks a running maxf (never decreases, only grows)
       The window is valid when (size - maxf) <= k. The window only grows or slides.
       Time: O(n) | Space: O(1)

Key insight: window is valid if (window_size - max_freq_char) <= k,
meaning the minority characters can all be replaced within budget k.
"""

class Solution:
    def characterReplacement1(self, s: str, k: int) -> int:
        """
        Sliding window: shrink the window when (window_size - max_freq) > k,
        meaning we'd need more than k replacements to make all chars the same.
        Uses max(map_ct.values()) on every iteration to find the dominant char.

        Time: O(n * 26) — O(n) window iterations, each calling max() over at most 26 keys
        Space: O(26) = O(1) — frequency map bounded by alphabet size
        """
        map_ct = {}
        ret = 0
        l =0
        for r in range(len(s)):
            map_ct[s[r]] = 1 + map_ct.get(s[r], 0)
            while (r-l+1) - max(map_ct.values()) > k:
                map_ct[s[l]] -=1
                l +=1

            ret = max(ret, r - l + 1)
        return ret

    def characterReplacement2(self, s: str, k: int) -> int:
        """
        Optimized sliding window: tracks max frequency seen so far (maxf) instead
        of recomputing max each iteration. The window only ever grows or slides,
        so maxf never needs to decrease — we only care about finding a longer window.

        Time: O(n) — single pass, O(1) work per step
        Space: O(26) = O(1) — frequency map bounded by alphabet size
        """
        count = {}
        l =0
        maxf = 0
        ret = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r-l+1) - maxf > k:
                count[s[l]] -=1
                l +=1
            
            ret = max(ret, (r - l + 1))

        return ret

if __name__ == '__main__':
    s1 = Solution()
    s, k = "ABCXYYX", 2
    print("Max length after char replacement is :{}".format(s1.characterReplacement1(s, k)))
    print("Max length after char replacement is :{}".format(s1.characterReplacement2(s, k)))

