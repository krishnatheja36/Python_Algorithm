"""
Top K Frequent Elements — LeetCode 347 | Arrays & Hashing

Logic:
    Count element frequencies with a hashmap, then sort the hashmap items by
    frequency in descending order. Collect the first k keys and return them.
    Alternative O(n) approach: bucket sort by frequency (index = count, max index = n).

Time:  O(n log n) — dominated by sorting the frequency map
Space: O(n) — hashmap and output list
"""

from collections import defaultdict
class Solution:
    def topKFrequent(self, nums, k):
        nums_hash = defaultdict(int)
        op = []
        for num in nums:
            nums_hash[num] +=1

        # print(nums_hash)
        for key, value in sorted(nums_hash.items(), key=lambda item: item[1], reverse=True):
            if k == 0:
                break
            else:
                op.append(key)
                k -= 1
        return nums_hash, op
if __name__ == '__main__':
    s1 = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    nums_hash, op = s1.topKFrequent(nums, k)
    print("Input list       : {}".format(nums))
    print("Hash couter      : {}".format(nums_hash))
    print("Top k elements   : {}".format(op))
