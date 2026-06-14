"""
Encode and Decode Strings — LeetCode 271 | Arrays & Hashing

Logic:
    Encode: prefix each string with "<length>#<string>", so "we" becomes "2#we".
    Decode: scan for '#', read the integer before it to get the length, then slice
    exactly that many characters. This handles any characters including '#' in the string.

Time:  O(n) encode — O(total characters)
Time:  O(n) decode — single pass with two-pointer slicing
Space: O(n) — output string / list
"""

class Solution:

    def encode(self, strs):
        op_str = ''
        for s in strs:
            op_str += str(len(s)) + '#' + s
        return op_str

    def decode(self, s):
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res

if __name__ == '__main__':
    Input = ["we","say",":","yes","!@#$%^&*()"]
    s1 = Solution()
    s1_encoded = s1.encode(Input)
    print("Encoded string: {}".format(s1_encoded))
    s1_decoded = s1.decode(s1_encoded)
    print("Decoded string: {}".format(str(s1_decoded)))
