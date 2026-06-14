"""
Reverse Words in a String — LeetCode 151
https://leetcode.com/problems/reverse-words-in-a-string/

Logic:
    Strip leading/trailing spaces. Scan left to right collecting each
    whitespace-delimited word. Prepend each word to a deque so the deque
    accumulates words in reverse order. Join with a single space and return.

Time:  O(n) — single pass through the stripped string
Space: O(n) — deque holds all words, proportional to input length
"""

from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        queue = deque([])
        i = 0
        s = s.strip()
        while i < len(s):
            if s[i] != " ":
                start = i
                while i<len(s) and s[i] != " ":
                    i +=1
                queue.appendleft(s[start:i])
                i -=1
            i+=1

        return " ".join(queue)

if __name__ == '__main__':
    S = Solution()
    string_to_reverse = ["Hello World",
                        "a   string   with   multiple   spaces",
                        "Case Sensitive Test 1234",
                        "a 1 b 2 c 3 d 4 e 5",
                        "     trailing spaces",
                        "case test interesting an is this"]

    for i in range(len(string_to_reverse)):
        print(i + 1, ".\tOriginal string: '" + "".join(string_to_reverse[i]), "'", sep='')
        Result = S.reverseWords(string_to_reverse[i])

        print("\tReversed string: '" + "".join(Result), "'", sep='')
        print("-" * 100)