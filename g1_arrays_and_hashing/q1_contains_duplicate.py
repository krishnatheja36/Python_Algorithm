"""
Contains Duplicate — LeetCode 217 | Arrays & Hashing

Logic:
    Iterate through the list, inserting each value into a hash set.
    If a value is already in the set, a duplicate exists — return True.
    If the loop completes without a hit, return False.

Time:  O(n) — single pass through the list
Space: O(n) — hash set stores up to n elements
"""

class Solution:
    def hasDuplicate(self, int_list):
        int_set = set()
        for val in int_list:
            if val in int_set:
                return True
            else:
                int_set.add(val)
        return False

if __name__ == '__main__':
    nums1 = [1, 2, 3, 3]
    S1 = Solution()
    print("List {} contains duplicates: {}".format(nums1,S1.hasDuplicate(nums1)))
    nums2 = [1, 2, 3, 4]
    print("List {} contains duplicates: {}".format(nums2,S1.hasDuplicate(nums2)))