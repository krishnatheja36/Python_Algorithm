"""
Letter Case Permutation — LeetCode 784
https://leetcode.com/problems/letter-case-permutation/

Logic:
    Start with [""] and process each character. For digits, append the character
    to every existing string. For letters, double the result list by appending
    both the lowercase and uppercase versions to each existing string.

Time:  O(n * 2^n) — up to 2^n strings, each of length n
Space: O(n * 2^n) — all permutations stored in the result list
"""

class Solution:
    def letter_case_permutation(self, s: str) -> list[str]:
        result = [""]

        for ch in s:
            print(result)
            if ch.isalpha():
                result = [str + ch.lower() for str in result] + [str + ch.upper() for str in result]
            else:
                result = [str + ch for str in result]
        
        return result
    

if __name__ == "__main__":
    S = Solution()
    strings = [
        "a1b2",   
        "3z4",   
        "ABC",  
        "123",  
        "xYz"   
    ]

    i = 0
    for s in strings:
        print(i + 1, ".\ts: ",'"', s,'"', sep="")
        print("\n\tOutput: ", S.letter_case_permutation(s), sep="")
        print("-" * 100)
        i += 1