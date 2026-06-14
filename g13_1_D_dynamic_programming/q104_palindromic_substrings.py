"""
Palindromic Substrings — LeetCode 647 | 1-D Dynamic Programming

Logic (expand around center — same technique as q103):
    For each index i, expand outward for both odd and even centered palindromes.
    Increment the count for every valid palindrome found during expansion.
    palindromic_substrings2 refactors into a helper for cleaner code.

Time:  O(n²) — n centers × O(n) expansion
Space: O(1)
"""

class Solution:

    def palindromic_substrings(self, s:str) -> str:
        res = 0
        
        for i in range(len(s)):
            # odd palindrome
            l, r = i, i
            while l >= 0 and  r<len(s) and s[l] == s[r]:
                res +=1
                l -=1
                r +=1
            
            # even palindrom    
            l, r = i, i+1
            while l >= 0 and  r<len(s) and s[l] == s[r]:
                res +=1
                l -=1
                r +=1
    
        return res

    def palindromic_substrings2(self, s:str) -> int:
        res = 0

        def helper(l, r):
            nonlocal res
            while l>=0 and r<len(s) and s[l] == s[r]:
                res +=1
                l -=1
                r +=1

        for i in range(len(s)):
            l,r = i,i
            helper(l,r)
            l,r = i, i+1
            helper(l,r)
              
        return res

if __name__ == "__main__":
    S = Solution()
    inputs = ["abc", "aaa", "abbc"]
    for s in inputs:
        print(f"Longest palindrome in '{s}' is '{S.palindromic_substrings(s)}'")
        print(f"Longest palindrome in '{s}' is '{S.palindromic_substrings2(s)}'")
