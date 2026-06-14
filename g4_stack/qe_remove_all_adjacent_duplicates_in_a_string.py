"""
Remove All Adjacent Duplicates In String — LeetCode 1047
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

Logic:
    Use a stack to process the string one character at a time. If the stack is
    non-empty and its top character equals the current character, pop the top
    (removing the adjacent duplicate pair). Otherwise push the current character.
    Join the stack at the end to form the result.

Time:  O(n) — each character is pushed and popped at most once
Space: O(n) — the stack can hold up to n characters in the worst case
"""

class Solution:

    def remove_duplicates(self, s):
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)


# Driver code
if __name__ == "__main__":
    S = Solution()
    inputs = ["g", 
        "ggaabcdeb", 
        "abbddaccaaabcd",
        "aannkwwwkkkwna", 
        "abbabccblkklu"
    ]

    for i in range(len(inputs)):
        print(i + 1, ".\tRemove duplicates from string: '", inputs[i], "'", sep = "")
        resulting_string = S.remove_duplicates(inputs[i])
        print("\tString after removing duplicates: ", resulting_string, sep = "")
        print('-'*100)

