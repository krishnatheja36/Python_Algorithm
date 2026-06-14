"""
Minimum Remove to Make Valid Parentheses — LeetCode 1249
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/

Logic:
    Convert the string to a list for in-place modification. Iterate through each
    character: if ')' is seen and the top of the stack is '(', pop it (matched pair).
    Otherwise push unmatched '(' or ')' with their indices. After the pass, blank
    out all characters at indices still in the stack, then join and return.

Time:  O(n) — two passes through the string
Space: O(n) — stack and character list each use O(n) space
"""

def min_remove_parentheses(s):
    stack = []
    s_list = list(s)
    
    for i, val in enumerate(s):
        if len(stack) > 0 and stack[-1][0] == '(' and val == ')':
            stack.pop()

        elif val == '(' or val == ')':
            stack.append([val, i])
    
    print(stack)

    for p in stack:
        s_list[p[1]] = ""
    
    result = ''.join(s_list)
   
    return result

# Driver code
if __name__ == "__main__":
    inputs = ["ar)ab(abc)abd(", "a)rt)lm(ikgh)", "aq)xy())qf(a(ba)q)", 
    "(aw))kk())(w(aa)(bv(wt)r)",  "(qi)(kl)((y(yt))(r(q(g)s)"]
    for i in range(len(inputs)):
        print(i + 1, ". Input: \"", inputs[i], "\"", sep="")
        print("   Valid parentheses, after minimum removal: \"", \
         min_remove_parentheses(inputs[i]), "\"", sep="")
        print("-" * 100)
