"""
Design Twitter — LeetCode 355 | Heap / Priority Queue

Logic:
    tweetMap: userId → list of [timestamp, tweetId] (timestamp decrements so lower = newer).
    followMap: userId → set of followeeIds (user always follows themselves for feed generation).
    getNewsFeed: seed a min-heap with the most recent tweet from each followee.
    Pop the most recent tweet, add it to results, then push that followee's next tweet.
    Repeat until 10 tweets are collected or heap is empty.

Time:  postTweet O(1) | follow/unfollow O(1) | getNewsFeed O(F log F + 10 log F), F = followees
Space: O(U + T) — U users, T total tweets
"""

from collections import defaultdict
import heapq
class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


if __name__ == "__main__":
    Input = ["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1], "getNewsFeed", [2], "unfollow", [1, 2], "getNewsFeed", [1]]
    twitter = Twitter()
    print(twitter.postTweet(1, 10)) # User 1 posts a new tweet with id = 10.
    print(twitter.postTweet(2, 20)) # User 2 posts a new tweet with id = 20.
    print(twitter.getNewsFeed(1))  # User 1's news feed should only contain their own tweets -> [10].
    print(twitter.getNewsFeed(2))  # User 2's news feed should only contain their own tweets -> [20].
    print(twitter.follow(1, 2))    # User 1 follows user 2.
    print(twitter.getNewsFeed(1))  # User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
    print(twitter.getNewsFeed(2))  # User 2's news feed should still only contain their own tweets -> [20].
    print(twitter.unfollow(1, 2))  # User 1 unfollows user 2.
    print(twitter.getNewsFeed(1))


