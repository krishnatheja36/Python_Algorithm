"""
Design Hit Counter — Karat / LeetCode 362 | Sliding Window

Pattern: Sliding Window with deque
  Maintain a deque of timestamps of hits. On getHits(t), evict all timestamps
  from the front that are more than 300 seconds old (t - front >= 300).
  The length of the remaining deque is the hit count in the last 5 minutes.

Time:  O(1) amortized — each timestamp pushed and popped at most once
Space: O(n) — n = max hits in a 300-second window
"""
from collections import deque


class HitCounter:
    def __init__(self):
        self.q = deque()

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)

    def get_hits(self, timestamp: int) -> int:
        while self.q and timestamp - self.q[0] >= 300:
            self.q.popleft()
        return len(self.q)


if __name__ == "__main__":
    ct = HitCounter()
    ct.hit(1); ct.hit(2); ct.hit(3)
    print(ct.get_hits(4))    # 3
    ct.hit(300)
    print(ct.get_hits(300))  # 4
    print(ct.get_hits(301))  # 3
