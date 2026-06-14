"""
Valid Palindrome — LeetCode 125 | Two Pointers

Logic:
    Two pointers starting at both ends of the string. Skip non-alphanumeric
    characters by advancing the respective pointer. Compare the lowercased
    characters at each pointer; if they differ, it's not a palindrome.
    Custom isAlNum avoids importing re or calling str.isalnum.

Time:  O(n) — each character visited at most once
Space: O(1) — no extra storage
"""

class Solution:
    def isPalindrome(self, s):
        i, j = 0, len(s) -1
        while i < j:
            while not self.isAlNum(s[i]) and i < j:
                i += 1
            while not self.isAlNum(s[j]) and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True
    def isAlNum(self, c):
        return(
                (ord('A') <= ord(c) <= ord('Z')) or \
                (ord('a') <= ord(c) <= ord('z')) or \
                (ord('0') <= ord(c) <= ord('9')) \
            )

if __name__ == '__main__':
    # print("A: {}, Z: {},a :{}, z:{}, 0: {}, 9: {}".format(ord('A'), ord('Z'), ord('a'), ord('z'), ord('0'), ord('9')))
    # # print("Given string \"{}\" is a Palindrome: {}".format(s, s1.isPalindrome(s)))
    s1 = Solution()
    s = ".,"
    print("Given string \"{}\" is a Palindrome: {}".format(s, s1.isPalindrome(s)))
