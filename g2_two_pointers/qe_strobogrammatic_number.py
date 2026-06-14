"""
Strobogrammatic Number — LeetCode 246
https://leetcode.com/problems/strobogrammatic-number/description/

Logic:
    Use a map of valid strobogrammatic digit pairs: {0:0, 1:1, 8:8, 6:9, 9:6}.
    Two pointers meet in the middle; at each step verify the outer characters
    form a valid pair. Return False immediately on any mismatch.

Time:  O(n) — each character is checked at most once
Space: O(1) — only the fixed map and two pointer variables are used
"""

class Solution:
    def is_strobogrammatic(self, num: str) -> bool:
        map = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}

        i, j = 0, len(num)-1
        while i<=j:
            if num[i] in map and  map[num[i]] == num[j]:
                i +=1
                j -=1
            else:
                return False
        return True


if __name__ == '__main__':
    S = Solution()
  
    nums = [
        "609",   
        "88",   
        "962",  
        "101",  
        "123"   
    ]

    i = 0
    for num in nums:
        print(i + 1, ".\tnum: ", num, sep="")
        print("\n\tIs strobogrammatic: ", S.is_strobogrammatic(num), sep="")
        print("-" * 100)
        i += 1
