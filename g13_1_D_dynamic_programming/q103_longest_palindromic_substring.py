"""
Longest Palindromic Substring — LeetCode 5 | 1-D Dynamic Programming

Logic (expand around center):
    For each index i, expand outward for both odd-length (center at i)
    and even-length (center between i and i+1) palindromes.
    Track the longest palindrome found by comparing r - l + 1 to resLen.
    longest_palindrome2 refactors the expansion into a helper to reduce duplication.

Time:  O(n²) — n centers × O(n) expansion per center
Space: O(1) — only pointers and result string tracked
"""

class Solution:
    def longest_palindrome(self, s:str) -> str:
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            # odd palindrome
            l, r = i, i
            while l >= 0 and  r<len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -=1
                r +=1
            
            # even palindrom    
            l, r = i, i+1
            while l >= 0 and  r<len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -=1
                r +=1
    
        return res
    
    def longest_palindrome2(self, s:str) -> str:
        res = ""
        resLen = 0

        def helper(l, r):
            nonlocal res            # Use nonlocal to access variable from the outer function
            nonlocal resLen
            while l >= 0 and  r<len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -=1
                r +=1

        for i in range(len(s)):
            l, r = i, i
            helper(l, r)            
            l, r = i, i+1
            helper(l,r)
        return res

if __name__ == "__main__":
    S = Solution()
    inputs = ["ababd", "abbc"]
    for s in inputs:
        print(f"Longest palindrome in '{s}' is '{S.longest_palindrome(s)}'")
        print(f"Longest palindrome in '{s}' is '{S.longest_palindrome2(s)}'")
