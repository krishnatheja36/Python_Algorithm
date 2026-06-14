"""
Restore IP Addresses — LeetCode 93
https://leetcode.com/problems/restore-ip-addresses/description/

Logic:
    Backtrack over the string placing 4 dot-separated segments. For each segment,
    try lengths 1–3 characters; reject if the value ≥ 256 or has a leading zero.
    When 4 dots are placed and the entire string is consumed, record the IP.

Time:  O(1) — at most 3^4 = 81 combinations to try (bounded input length ≤ 12)
Space: O(1) — constant number of recursive frames and candidates
"""

class Solution:
    def restore_ip_addresses(self, s: str) -> list[str]:
        res = []

        if len(s) >12:
            return res

        def backtrack(i, dots, curIP):
            if dots ==4 and i ==len(s):
                res.append(curIP[:-1])
                return
            if dots >4:
                return

            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1]) <256 and ((i==j) or s[i] != '0'):
                    backtrack(j+1, dots+1, curIP + s[i:j+1]+'.')
        backtrack(0,0,"")
        return res

if __name__ == '__main__':
    S = Solution()
    ip_addresses = ["0000", "25525511135", "12121212",
                    "113242124", "199219239", "121212", "25525511335"]

    for i in range(len(ip_addresses)):
        print(i + 1, ".\t Input addresses: '", ip_addresses[i], "'", sep="")
        print("\t Possible valid IP Addresses are: ",
              S.restore_ip_addresses(ip_addresses[i]), sep="")
        print("-" * 100)
