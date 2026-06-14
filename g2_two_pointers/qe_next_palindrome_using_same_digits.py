"""
Next Palindrome Using Same Digits — Two Pointers

Two approaches:

  1. find_next_palindrome — next-permutation on the left half:
       Advance the left half to its next lexicographic permutation, then mirror
       it to form the next palindrome. Return "" if no permutation exists or the
       result is not strictly greater than the input.
       Time: O(n) | Space: O(n) — operates on a list copy of the left half

  2. find_next_palindrome_new — brute-force permutations:
       Generate all permutations of the digits, filter for palindromes greater
       than the input, and return the smallest such value.
       Time: O(n! * n) | Space: O(n! * n) — all permutations stored
"""

from itertools import permutations

class Solution:

    def find_next_permutation(self, digits):
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        if i == -1:
            return False

        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1

        digits[i], digits[j] = digits[j], digits[i]
        digits[i + 1:] = reversed(digits[i + 1:])
        return True

    def find_next_palindrome(self, num_str):
        n = len(num_str)

        if n == 1:
            return ""

        half_length = n // 2
        left_half = list(num_str[:half_length])

        if not self.find_next_permutation(left_half):
            return ""

        if n % 2 == 0:
            next_palindrome = ''.join(left_half + left_half[::-1])
        else:
            middle_digit = num_str[half_length]
            next_palindrome = ''.join(left_half + [middle_digit] + left_half[::-1])

        if next_palindrome > num_str:
            return next_palindrome
        return ""

    def find_next_palindrome_new(self, num_str):
        c = []
        for combo in sorted(permutations(list(num_str), len(num_str))):
            val = ''.join(combo)
            if int(val)>int(num_str) and val== ''.join(reversed(list(combo))):
                return val
        return ''


if __name__ == "__main__":

    S = Solution()

    test_cases = ["1221", "54345", "999", "12321", "89798"]

    for i in range(len(test_cases)):
        print(i + 1, ".\t Original palindrome: '", test_cases[i], "'", sep="")
        next_palindrome = S.find_next_palindrome(test_cases[i])
        print(f"\t Next greater palindrome: '{next_palindrome}'", sep="")
        next_palindrome = S.find_next_palindrome_new(test_cases[i])
        print(f"\t Next greater palindrome: '{next_palindrome}'", sep="")
        print("-" * 100)
