"""
Min Stack — LeetCode 155 | Stack

Logic (implemented — single stack, linear getMin):
    Regular list for push/pop/top. getMin calls min() on the entire stack — O(n).

Optimal approach:
    Use a second parallel "min stack" that tracks the current minimum at each push.
    When pushing val, also push min(val, minStack[-1]) onto the min stack.
    getMin then returns minStack[-1] in O(1).

Time:  push/pop/top O(1), getMin O(n) — current implementation
Space: O(n)
Optimal getMin: O(1)
"""

class MinStack:

    def __init__(self):
        self.int_stack = []

    def push(self, val: int) -> None:
        self.int_stack.append(val)

    def pop(self) -> None:
        self.int_stack.pop()

    def top(self) -> int:
        return self.int_stack[-1]

    def getMin(self) -> int:
        return min(self.int_stack)

    def print_stack(self):
        print("Current Stack :", self.int_stack)

if __name__ == '__main__':
    minStack = MinStack();
    print("Pushing value 1 :", minStack.push(1))
    minStack.print_stack()
    print("Pushing value 2 :", minStack.push(2))
    minStack.print_stack()
    print("Pushing value 2 :", minStack.push(0))
    minStack.print_stack()
    print("Get min :", minStack.getMin())
    minStack.print_stack()
    print("Run Pop :", minStack.pop())
    minStack.print_stack()
    print("Run top :", minStack.top())
    minStack.print_stack()
    print("Get min :", minStack.getMin())
    minStack.print_stack()

