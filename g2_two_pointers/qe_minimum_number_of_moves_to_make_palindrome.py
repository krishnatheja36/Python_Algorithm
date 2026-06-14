"""
Minimum Number of Moves to Make Palindrome — LeetCode 2193
https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

Logic:
    Use two pointers (i from left, j from right). If s[i] == s[j] both advance.
    Otherwise find the matching character for s[i] scanning inward from j, then
    swap it toward j counting each swap. If no match exists (odd-length middle
    character), count the swaps needed to move it to the center.

Time:  O(n^2) — for each outer step, inner search and swaps can take O(n)
Space: O(n) — string is converted to a list for in-place swaps
"""

class Solution:
    def min_moves_to_make_palindrome(self, s: str) -> int:
        s = list(s)
        i, j, r = 0, len(s)-1, len(s)-1
        count = 0
        while i < j:
            if s[i] == s[j]:
                i +=1
                j -=1
            else:
                r = j
                while s[r] != s[i]:
                    r -=1
                if r == i:
                    count += ((len(s) // 2) - i)
                    i +=1
                else:
                    while r < j:
                        s[r], s[r+1] = s[r+1], s[r]
                        r +=1
                        count +=1
        print(s)
        return count




if __name__ == '__main__':
    S = Solution()
    strings = ["ccxx", "arcacer", "w", "ooooooo", "eggeekgbbeg"]
    
    for index, string in enumerate(strings):
        print(f"{index + 1}.\ts: {string}")
        print(f"\tMoves: {S.min_moves_to_make_palindrome(string)}")
        print('-' * 100)
