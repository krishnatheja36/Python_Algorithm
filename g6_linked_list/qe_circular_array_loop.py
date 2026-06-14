"""
Circular Array Loop — LeetCode 457
https://leetcode.com/problems/circular-array-loop/description/

Logic:
    For each starting index, run a fast/slow pointer search. Both pointers follow
    the cyclic step formula (pointer + nums[pointer]) % size. A valid cycle must
    maintain a consistent direction (all positive or all negative) and length > 1
    (detected by checking if the step modulo size is 0). Return True if slow == fast.

Time:  O(n^2) — outer loop over n starting points; inner traversal can be O(n)
Space: O(1) — only pointer variables used
"""

class Solution:
    def circular_array_loop(self, nums):
        size = len(nums)
        
        for i in range(size):
            slow = fast = i
            forward = nums[i] > 0
        
            while True:
                slow = self.next_step(slow, nums[slow], size) 
                if self.is_not_cycle(nums, forward, slow):
                    break
            
                fast = self.next_step(fast, nums[fast], size)
                if self.is_not_cycle(nums, forward, fast):
                    break
                
                fast = self.next_step(fast, nums[fast], size)
                if self.is_not_cycle(nums, forward, fast):
                    break
            
                if slow == fast:
                    return True
                    
        return False

    # A function to calculate the next step
    def next_step(self, pointer, value, size):
        return (pointer + value) % size


    # A function to detect a cycle doesn't exist
    def is_not_cycle(self, nums, prev_direction, pointer):
        curr_direction = nums[pointer] >= 0
        
        if (prev_direction != curr_direction) or (nums[pointer] % len(nums) == 0):
            return True
        else:
            return False

# Driver code
def main():
    S = Solution()
    input = (
            [-2, -3, -9],
            [-5, -4, -3, -2, -1],
            [-1, -2, -3, -4, -5],
            [2, 1, -1, -2],
            [-1, -2, -3, -4, -5, 6],
            [1, 2, -3, 3, 4, 7, 1],
            [2, 2, 2, 7, 2, -1, 2, -1, -1]
            )
    num = 1

    for i in input:
        print(f"{num}.\tCircular array = {i}")
        print(f"\n\tFound loop = {S.circular_array_loop(i)}")
        print("-"*100, "\n")
        num += 1


if __name__ == "__main__":
    main()