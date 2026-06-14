"""
Valid Parentheses — LeetCode 20 | Stack

Logic:
    Map each closing bracket to its expected open counterpart.
    Push opening brackets onto the stack. When a closing bracket is seen,
    check if the top of the stack is the matching open bracket — if not, invalid.
    At the end, the stack must be empty (all openers were closed).

Time:  O(n) — single pass
Space: O(n) — stack holds at most n/2 open brackets
"""

class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {'}':'{', ')':'(',']':'['}
        char_stack = []
        print(s)

        for c in s:
            print(char_stack)
            if c in closeToOpen:
                if (char_stack) and (char_stack[-1] == closeToOpen[c]):
                    char_stack.pop()
                else:
                    return False
            else:
                char_stack.append(c)

        return not char_stack


if __name__ == '__main__':
    s = "([{}])"
    S1 = Solution()
    print("Given string {} contains valid Paranthesis: {}".format(s, S1.isValid(s)))