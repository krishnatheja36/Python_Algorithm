"""
N-th Tribonacci Number — LeetCode 1137
https://leetcode.com/problems/n-th-tribonacci-number/description/

Logic:
    T(0)=0, T(1)=1, T(2)=1. For n ≥ 3 each term is the sum of the three
    preceding terms. Roll three variables forward in a single loop to avoid
    any array allocation.

Time:  O(n) — single pass computing n-2 iterations
Space: O(1) — only three rolling variables maintained
"""

class Solution:

    def find_tribonacci(self, n):
        if n < 3:
            return 1 if n else 0

        first_num, second_num, third_num = 0, 1, 1
        for _ in range(n - 2):
            first_num, second_num, third_num = second_num, third_num, (first_num + second_num + third_num)
        return third_num



if __name__ == '__main__':
    S = Solution()
    print("")
    n = [4, 5, 25, 17, 19]
    for i in range(len(n)):
        print((i + 1), ".\tThe ", (n[i]), "th Tribonacci number is:  ", S.find_tribonacci(n[i]), sep="")
        print("-"*100, "\n")


