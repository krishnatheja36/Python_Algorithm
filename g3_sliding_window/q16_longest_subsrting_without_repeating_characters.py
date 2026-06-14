"""
Longest Substring Without Repeating Characters — LeetCode 3 | Sliding Window

Two approaches:
  1. Brute force (lengthOfLongestSubstring1):
       For each start index i, expand a window until a repeat is found.
       Time: O(n^2) | Space: O(m) — m = character set size

  2. Sliding window (lengthOfLongestSubstring2):
       Maintain a set of characters in the current window [l, r].
       When s[r] repeats, shrink from the left until it's removed.
       Each character is added/removed at most once.
       Time: O(n) | Space: O(m)
"""

class Solution:
    # Time: O(n^2) — outer loop O(n), inner while can scan up to O(n) per start
    # Space: O(m) — m = size of character set (at most 26 for lowercase letters)
    def lengthOfLongestSubstring1(self, s):
        max_len = 0
        for i in range (len(s)):
            char_set = set()
            while i < len(s):
                if s[i] not in char_set:
                    char_set.add(s[i])
                    i +=1
                else:
                    break
            max_len = max(max_len, len(char_set))
        return max_len

    # Time: O(n) — each character is added and removed from the set at most once
    # Space: O(m) — m = size of character set (at most 26 for lowercase letters)
    def lengthOfLongestSubstring2(self, s):
        max_len = 0
        l = 0
        char_set = set()
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[r])
                l +=1
            char_set.add(s[r])
            max_len = max(max_len, r-l+1)
        return max_len

if __name__ == '__main__':
    s1 = Solution()
    s = "zxyzxyz"
    print("Max length in the given string :{} is :{}".format(s, s1.lengthOfLongestSubstring1(s)))
    s = "pwwkew"
    print("Max length in the given string :{} is :{}".format(s, s1.lengthOfLongestSubstring1(s)))
    s = " "
    print("Max length in the given string :\'{}\' is :{}".format(s, s1.lengthOfLongestSubstring1(s)))

    s = " "
    print("Max length in the given string :\'{}\' is :{}".format(s, s1.lengthOfLongestSubstring2(s)))





