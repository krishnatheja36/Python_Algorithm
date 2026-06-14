"""
Group Anagrams — LeetCode 49 | Arrays & Hashing

Logic:
    For each string, build a 26-element character-count array (index = ord(c) - ord('a')).
    Use that array (as a tuple) as a hashmap key — all anagrams of a word produce the
    same count array. Group strings by their key and return the groups.

Time:  O(n * m) — n strings, m = average string length
Space: O(n * m) — storing all strings across the groups
"""

from collections import  defaultdict

class Solution:
    def groupAnagrams(self, strs):
        summ_dict = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for s in str:
                count[ord(s) - ord('a')] +=1
            summ_dict[tuple(count)].append(str)
        return list(summ_dict.values())

if __name__ == '__main__':
    strs = ["act","pots","tops","cat","stop","hat"]
    s1 = Solution()
    ret = s1.groupAnagrams(strs)
    print("Grouped Anagram List: {}".format(ret))