"""
3Sum — LeetCode 15 | Two Pointers

Logic:
    Sort the array. Fix each element a (skipping duplicates); use two pointers
    l and r on the subarray to the right. If a > 0, no valid triplet can exist
    (all remaining are positive). On a match, advance both pointers and skip
    duplicate l values. Duplicate a values are skipped at the outer loop.

Time:  O(n^2) — O(n) outer loop × O(n) two-pointer inner scan
Space: O(1) excluding the output list (sort is in-place)
"""

class Solution:
    def threeSum(self, nums):
        op = []
        nums.sort()
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i >0  and a == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a +  nums[l] + nums[r]
                if threeSum > 0:
                    r -=1
                elif threeSum <0:
                    l +=1
                else:
                    op.append([a, nums[l], nums[r] ])
                    l +=1
                    r -=1
                    while nums[l] == nums[l -1] and l <r:
                        l +=1
        return op

if __name__ == '__main__':
    nums = [0, 1, 1]
    s1 = Solution()
    print("Three Sum op: {}".format(s1.threeSum(nums)))
    nums = [0, 0, 0]
    print("Three Sum op: {}".format(s1.threeSum(nums)))
    nums = [-1,0,1,2,-1,-4]
    print("Three Sum op: {}".format(s1.threeSum(nums)))