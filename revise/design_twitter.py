# https://leetcode.com/problems/design-twitter/description/

import itertools
import collections
import heapq
from collections import deque


class Twitter:
    def __init__(self):
        self.data = dict()
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        user_data = self.data.get(
            userId, {"feed": [], "tweets": dict(), "followers": [], "followed": []}
        )
        user_data["tweets"][tweetId] = self.timestamp
        user_data["feed"] = map(
            lambda x: x[0],
            [(v, k) for k, v in enumerate(user_data["tweets"])].sort(reverse=True)[:10],
        )
        self.data[userId] = user_data
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        return self.data[userId]["feed"]

    def follow(self, followerId: int, followeeId: int) -> None:
        # self.data[]
        pass

    def unfollow(self, followerId: int, followeeId: int) -> None:
        pass
