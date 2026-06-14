"""
Valid Word Abbreviation — LeetCode 408 | Two Pointers

Logic:
    Two pointers i (word) and j (abbreviation) advance together. If abbr[j] is
    a letter, it must match word[i]; both advance. If abbr[j] is a digit, reject
    leading zeros immediately, then accumulate the full number and skip that many
    characters in word. Both pointers must be exhausted simultaneously.

Time:  O(n) — single pass through both strings
Space: O(1) — only pointer and counter variables are used
"""

# #################################################################################################################################################
# Valid Word Abbreviation
# #################################################################################################################################################
# Statement
# Given a string, word, and abbreviation, abbr, return TRUE if the abbreviation matches the given string. Otherwise, return FALSE. An abbreviation can replace any non-adjacent, non-empty substrings of the original word with their lengths. Replacement lengths must not contain leading zeros.
# A certain word, "calendar", can be abbreviated as follows:
# •	"cal3ar" ("cal + end [length = 3] + ar" skipping three characters "end" from the word "calendar" still matches the provided abbreviation)
# •	"c6r" ("c + alenda [length = 6] + r" skipping six characters "alenda" from the word "calendar" still matches the provided abbreviation)
# The word "internationalization" can also be abbreviated as "i18n" (the abbreviation comes from skipping 18 characters in "internationalization" leaving the first and last letters "i" and "n").
# #################################################################################################################################################
# The following are not valid abbreviations:
# •	"c06r" (Has leading zeroes)
# •	"cale0ndar" (Replaces an empty string)
# •	"c24r" ("c al enda r" the replaced substrings are adjacent)
# #################################################################################################################################################
# Constraints:
# •	1≤1≤ word.length ≤20≤20
# •	The word consists of only lowercase English letters.
# •	1≤1≤ abbr.length ≤10≤10
# •	abbr consists of lowercase English letters and digits.
# •	All the integers in abbr will fit in a 3232–bit integer.
# #################################################################################################################################################

class Solution:
    def valid_word_abbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while j < len(abbr):
            if i >= len(word):
                return False
            if abbr[j].isalpha():
               if abbr[j] != word[i]:
                   return False
               else:
                   j +=1
                   i +=1
            elif int(abbr[j]) ==0:
                return False
            else:
                ct =0
                while j <len(abbr) and not(abbr[j].isalpha()):
                    j +=1
                    ct +=1
                i +=int(abbr[j-ct: j])


        if i ==len(word) and j ==len(abbr):
            return True
        else:
            return False


if __name__ == '__main__':
    S = Solution()
    
    words = ["a", "a", "abcdefghijklmnopqrst", "abcdefghijklmnopqrst", "word", "internationalization", "localization"]
    abbreviations = ["a", "b", "a18t", "a19t", "w0rd", "i18n", "l12n"]

    for i in range(len(words)):
        print(i + 1, ".\t word: '", words[i], "'", sep="")
        print("\t abbr: ", abbreviations[i], "'", sep="")
        print(f"\n\t Is '{abbreviations[i]}' a valid abbreviation for the word '{words[i]}'? ", S.valid_word_abbreviation(words[i], abbreviations[i]), sep="")
        print("-" * 100)