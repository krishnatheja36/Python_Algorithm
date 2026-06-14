"""
Word Break II — LeetCode 140
https://leetcode.com/problems/word-break-ii/description/

Logic:
    Backtracking (DFS) with a word set for O(1) lookup. At position i, try every
    prefix s[i:j+1]; if it is in the word set, recurse from j+1 with the word
    appended to the current path. When the end of string is reached, join the
    path with spaces and record it.

Time:  O(2^n * n) — worst case; exponential paths, each taking O(n) to join
Space: O(2^n * n) — result list can hold exponentially many sentences
"""

class Solution:

    def word_break(self, s, word_dict):
        word_dict = set(word_dict)

        def bfs(i):
            if i ==len(s):
                res.append(" ".join(cur))
                return
            for j in range(i, len(s)):
                w = s[i:j+1]
                if w in word_dict:
                    cur.append(w)
                    bfs(j+1)
                    cur.pop()

        res = []
        cur = []
        bfs(0)
        return res


# Driver Code
if __name__ == "__main__":
    S = Solution()
    
    s = ["vegancookbook", "catsanddog", "highwaycrash",
         "pineapplepenapple", "screamicecream", "educativecourse"]

    word_dict = ["oghi", "ncoo", "kboo", "inea",
        "icec", "ghway", "tsand", "anco", "eame", "ghigh", "hi", "way", "wa",
        "amic", "mi", "ed", "cecre", "pple", "reamicecreamed", "ena", "tsa", "ami", "hwaycrashpineapplepenapplescreamicecreamed", "lepen", "okca", "highway", "ples", "atsa", "oghig", "ookb", "epe", "ookca", "nea", "cra", "lepe", "vegancookbookcatsandd",
        "kc", "ra", "le", "ay", "crashpineapple", "ycras", "vegancookbookcatsanddoghighwaycrashpineapplepenapplescre", "doghi", "nddo", "hway", "vegancookbookcatsanddoghi", "vegancookbookcatsanddoghighwaycr", "at", "mice", "nc", "d", "enapplescreamicecreamed", "h",
        "ecrea", "nappl", "shp", "kbo", "yc", "vegancookbookcatsanddoghighwaycrashpineapplepenapplescream", "cat", "waycrashpineapplepenapplescreamicecreamed", "tsan", "vegancookbookcatsanddoghighwaycrashpineap", "ganco", "lescr", "sand", "applescreamicecreamed", "vegancookbookcatsanddoghig", "pi", "vegancookbookcatsanddoghighwaycrashpineapp", "cookb", "okcat", "neap", "nap", "oghighwaycrashpineapplepenapplescreamicecreamed", "crashpineapplepenapplescreamicecreamed",
        "ashpi", "ega", "escreamicecreamed", "hwa", "rash", "cre", "micecreamed", "plepe", "coo", "epen", "napp", "wayc", "vegancookbookcatsanddoghighwaycrashpinea", "vegancookbookcatsanddogh", "plep", "ice", "ple", "gh", "ghw", "cook", "pl", "app", "ic", "pinea", "hello", "dog", "vegancookbookcat", "eamed", "ook", "lesc", "ddog", "ca", "vegancookbookcatsanddoghighwaycrashpineapplepenapplescreamice", "c", "escr", "penap", "boo", "eami", "ecreamed", "vegancookbookcatsanddoghighwaycrashpi", "igh", "mic", "ganc", "vegancookbookcatsanddoghighwaycrashpineapplepenap",
        "eappl", "vegancookbookcatsanddoghighway", "ep", "penapple", "b", "ycrashpineapplepenapplescreamicecreamed", "pin", "book", "p", "sa", "okb", "andd", "ayc", "sh", "vegan", "cookbook"]

    print("The list of words we can use to break down the strings are:\n\n", word_dict, "\n")
    print("-" * 100)
    for i in range(len(s)):
        print("Test Case #", i+1, "\n\nThe possible strings from the string '" +
              str(s[i]) + "' are the following combinations:", sep="")
        print("\n" + str(S.word_break(str(s[i]), word_dict)))
        print("-" * 100)
