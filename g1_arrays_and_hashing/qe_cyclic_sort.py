"""
Cyclic Sort — qe | Arrays & Hashing

Logic:
    For arrays with values in range [1, n], each value belongs at index value-1.
    Iterate through the array; if nums[i] is not at its correct index, swap it
    with the element at nums[i]-1. Only advance i when the current element is
    already in the correct position.

Time:  O(n) — each element is moved to its correct index at most once
Space: O(1) — sorting is done in-place with no extra data structures
"""

class Solution:
    def cyclic_sort(self, nums):
        i = 0
        while i < len(nums):
            correct = i +1
            if nums[i] != correct:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i +=1

        return nums

if __name__ == '__main__':
    S = Solution()
    print("-" * 100, "\nSolution:\n", "-" * 100, sep="")
    test_cases = [
        [3, 1, 5, 4, 2],
        [4, 3, 2, 1, 5, 6],
        [1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1]
    ]

    for i, nums in enumerate(test_cases):
        print(f"{i + 1}. Input:  {nums}")
        S.cyclic_sort(nums)
        print(f"   Output: {nums}")
        print("-" * 100)

