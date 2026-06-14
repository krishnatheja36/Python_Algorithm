"""
Subsets — LeetCode 78 | Backtracking

Given an integer array nums of unique elements, return all possible subsets
(the power set). The solution set must not contain duplicate subsets.

Logic:
    subsets1 (DFS/Backtracking):
        At each index, branch into two recursive calls — one that includes
        nums[n] in the current subset and one that excludes it. When the
        index reaches len(nums) we have made a decision for every element,
        so we record a copy of the current subset. This traverses a binary
        decision tree of depth n, visiting every leaf exactly once.

    subsets2 (Iterative/BFS):
        Start with the empty subset. For each number, extend every existing
        subset by appending that number, then add all new subsets to the
        result. After processing k numbers the result holds all 2^k subsets
        of the first k elements.

Time:  O(n * 2^n) — 2^n subsets, each up to length n to copy
Space: O(n) — recursion stack depth for subsets1; O(1) extra for subsets2
"""
class Solution:
    def subsets1(self, nums: list[int]) -> list[list[int]]:
        result = []
        subsets = []
        def dfs(n):
            if n == len(nums):
                result.append(subsets[:])
                return

            subsets.append(nums[n])
            dfs(n+1)

            subsets.pop()
            dfs(n+1)

        dfs(0)
        return result

    def subsets2(self, nums:list[int]) -> list[list[int]]:
        result = [[]]
        for num in nums:
            curr = [subset + [num] for subset in result]
            result += curr
        return result



if __name__ == "__main__":
    nums = [1,2,3]
    # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    S = Solution()
    print(S.subsets1(nums=nums))
    print(S.subsets2(nums=nums))