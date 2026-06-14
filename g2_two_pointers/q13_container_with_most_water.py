"""
Container With Most Water — LeetCode 11 | Two Pointers

Logic:
    Start with l and r at both ends (widest possible container).
    Area = min(h[l], h[r]) * (r - l). Move the pointer at the shorter height
    inward — the shorter side is the limiting factor; moving the taller one
    can only decrease or maintain width while the height stays the same.
    Track the max area seen across all positions.

Time:  O(n) — l and r meet in the middle
Space: O(1)
"""

class Solution:
    def maxArea(self, heights):
        max_area = 0
        l, r = 0, len(heights)-1
        while l < r:
            area = min(heights[l], heights[r]) * (r -l)
            max_area = max(max_area, area)
            if heights[l] <= heights[r]:
                l +=1
            else:
                r -=1
        return max_area

if __name__ == '__main__':
    height = [1, 7, 2, 5, 4, 7, 3, 6]
    s1 = Solution()
    print("Max area is :{}".format(s1.maxArea(height)))
    height = [2, 2, 2]
    print("Max area is :{}".format(s1.maxArea(height)))