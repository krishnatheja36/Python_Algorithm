"""
Count Days Without Meetings — LeetCode 3169
https://leetcode.com/problems/count-days-without-meetings/

Logic:
    Sort meetings by start day. Track the running end boundary (prev_end). For
    each meeting, clamp its start to max(begin, prev_end+1) so that already-counted
    days aren't double-subtracted, then subtract the remaining length from the
    total free days.

Time:  O(n log n) — sorting plus one linear pass
Space: O(1) — only pointer variables used
"""

class Solution:
    def count_days(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort()

        prev_end =0
        for begin, end in meetings:
            begin = max(begin, prev_end+1)
            len = end - begin +1
            len = max(len, 0)
            days -= len
            prev_end = max(prev_end, end)        
        
        return days

if __name__ == "__main__":
    S = Solution()
    input_days = [12, 6, 100000, 3136, 786]
    input_meetings = [
        [[5, 6], [9, 11], [1, 3]],
        [[2, 4], [5, 5]],
        [[1, 100000]],
        [[361, 570], [420, 1225], [72, 144], [987, 1444]],
        [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]
    ]
    
    for i, (days, meetings) in enumerate(zip(input_days, input_meetings), 1):
        print(f"{i}.\tdays: {days}")
        print("\tmeetings:", meetings)
        print(f"\n\tNumber of free days: {S.count_days(days, meetings)}")
        print('-' * 100)
