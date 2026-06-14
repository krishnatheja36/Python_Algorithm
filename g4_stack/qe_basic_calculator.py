"""
Basic Calculator — LeetCode 224
https://leetcode.com/problems/basic-calculator/description/

Logic:
    Iterate through the expression character by character. Accumulate multi-digit
    numbers and apply the current sign when a +/- operator is seen. On '(' push
    the running result and current sign onto a stack, then reset them for the
    nested sub-expression. On ')' finalize the inner result, multiply by the
    popped sign, and add the popped outer result.

Time:  O(n) — single pass through the expression string
Space: O(n) — stack depth proportional to the nesting level of parentheses
"""

class calculate:

    def calculator(self, expression):
        number = 0
        sign_value = 1
        result = 0
        operations_stack = []

        for c in expression:
            if c.isdigit():
                number = number * 10 + int(c)
            if c in "+-":
                result += number * sign_value
                sign_value = -1 if c == '-' else 1
                number = 0
            elif c == '(':
                operations_stack.append(result)
                operations_stack.append(sign_value)
                result = 0
                sign_value = 1

            elif c == ')':
                result += sign_value * number
                pop_sign_value = operations_stack.pop()
                result *= pop_sign_value

                second_value = operations_stack.pop()
                result += second_value
                number = 0
        
        return result + number * sign_value
    
# Driver code
def main():
    S = calculate()
    input = (
             "4 + (52 - 12) + 99",
             "(31 + 7) - (5 - 2)",
             "(12 - 9 + 4) + ( 7 - 5)",
             "8 - 5 + (19 - 11) + 6 + (10 + 3)",
             "56 - 44 - (27 - 17 - 1) + 7"
            )

    num = 1
    for i in input:
        # Set to False to supress line-by-line trace
        print(num, ".", "\tGiven Expression: ", i, sep="")
        print("\tThe result is: ", S.calculator(i))
        num += 1
        print("-"*100, sep="")


if __name__ == "__main__":
    main()
