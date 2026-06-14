"""
Car Fleet — LeetCode 853 | Stack

Logic:
    Sort cars by position descending (closest to target first).
    Compute each car's time to reach target: (target - pos) / speed.
    Push each time onto the stack. If the newly pushed time is ≤ the one below it,
    the car catches up (merges into the fleet ahead) — pop it.
    Each entry remaining in the stack represents a distinct fleet.

Time:  O(n log n) — sorting dominates
Space: O(n) — stack
"""

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        print(pair)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

if __name__ == "__main__":
    S = Solution()
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    print("Car fleet at target: ", S.carFleet(target, position, speed))



        