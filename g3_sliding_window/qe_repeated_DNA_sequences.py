"""
Repeated DNA Sequences — LeetCode 187
https://leetcode.com/problems/repeated-dna-sequences/description/

Logic:
    Two approaches provided.
    Simple: slide a window of length 10 across the string; store each substring
    in a seen set and collect duplicates in a result set.
    Optimized (Rabin-Karp rolling hash): encode nucleotides as base-4 digits,
    compute the initial hash, then roll forward by removing the outgoing character
    contribution and adding the incoming one. Detect repeats via seen hashes.

Time:  O(n) — single pass with O(1) hash updates per step (rolling hash approach)
Space: O(n) — seen and output sets can hold up to O(n) entries
"""

class Solution:

    def findRepeatedDnaSequencesSimple(self, s: str) -> list[str]:
        seen, res = set(), set()

        for i in range(len(s)-9):
            if s[i:i+10] in seen:
                res.add(s[i:i+10])
            else:
                seen.add(s[i:i+10])

        return list(res)
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        L, n = 10, len(s)
        if n <= L:
            return []

        a = 4
        aL = pow(a, L)

        to_int = {"A": 0, "C": 1, "G": 2, "T": 3}
        nums = [to_int.get(s[i]) for i in range(n)]

        h = 0
        seen, output = set(), set()

        for start in range(n - L + 1):
            if start != 0:
                h = h * a - nums[start - 1] * aL + nums[start + L - 1]
            else:
                for i in range(L):
                    h = h * a + nums[i]
            if h in seen:
                output.add(s[start: start + L])
            seen.add(h)

        return output
    
if __name__=="__main__":
    S = Solution()
    test_cases = [
        "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
        "AAAAAAAAAAAAA",
        "ACGTACGTACGTACGTACGTACGTACGTACGT",
        "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
        "GTACGTACGTACGCCCCCCCCGGGGG",
    ]

    for i, s in enumerate(test_cases):
        print(f'{i+1}.\tInput: "{s}"')
        print(f"\n\tEncoded Output: {S.findRepeatedDnaSequencesSimple(s)}")
        print("-" * 100)
