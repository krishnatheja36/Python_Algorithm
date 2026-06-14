"""
First Bad Version — LeetCode 278
https://leetcode.com/problems/first-bad-version/description/

Logic:
    Binary search over version numbers [1, n]. If the midpoint is bad, the first
    bad version is at mid or earlier (move right boundary left). If good, it must
    be later (move left boundary right). Loop terminates when left == right, which
    is the first bad version.

Time:  O(log n) — binary search halves the search space each step
Space: O(1) — only two pointer variables used
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class BadVersion:
    def __init__(self, v):
        self.bad_version = v
    def is_bad_version(self, version):
        return version >= self.bad_version

class Solution(BadVersion):
    
    def first_bad_version(self, n: int) -> int:
        first = 1
        last = n
        
        while first <= last:  
            mid = first + (last - first) // 2;
    
            if self.is_bad_version(mid):  
                last = mid - 1
            else:
                first = mid + 1
            
        return first


if __name__ == '__main__':
    # S = Solution()
    versions = [6, 8, 9, 11, 8]
    bad_versions = [3, 5, 1, 11, 4]
    print("-" * 100, "\nSolution:\n", "-" * 100, sep="")

    for i in range(len(versions)):
        S = Solution(bad_versions[i])
        print(i + 1,  ".\tNumber of versions: ", versions[i], sep="")
        print("\tFirst bad version: ", S.first_bad_version(versions[i]))
        
        print("-"*100)