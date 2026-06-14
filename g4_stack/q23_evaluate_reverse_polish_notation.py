"""
Evaluate Reverse Polish Notation — LeetCode 150 | Stack

Logic:
    Scan tokens left to right. Push integers onto the stack.
    When an operator is encountered, pop the top two values, apply the operator
    (note: val1 is the deeper operand, val2 is the top), and push the result.
    Integer division truncates toward zero — use int() to handle negatives correctly.

Time:  O(n) — single pass through tokens
Space: O(n) — stack holds at most n/2 operands
"""

class Solution:
    def evalRPN(self, tokens) -> int:
        present_stack = []
        expr_list = ['+', '-', '*', '/']

        for e in tokens:
            if e not in expr_list:
                present_stack.append(int(e))
            else:
                if len(present_stack)>=2:
                    val2, val1 = present_stack.pop(), present_stack.pop()
                    res = int
                    if e == '+':
                        res = val1 + val2
                    elif e == '-':
                        res = val1 - val2
                    elif e == '*':
                        res = val1 * val2
                    elif e == '/':
                        res = val1 / val2
                    present_stack.append(int(res))
                else:
                    return None
        # print(present_stack)
        return present_stack[-1]

if __name__ == '__main__':
    S1 = Solution()
    tokens = ["1","2","+","3","*","4","-"]
    print(S1.evalRPN(tokens))
    tokens = ["4", "13", "5", "/", "+"]
    print(S1.evalRPN(tokens))