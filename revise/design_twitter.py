# https://leetcode.com/problems/design-twitter/description/

from itertools import count
import heapq
from collections import deque, defaultdict


class Twitter:
    def __init__(self):
        self.timer = count(step=-1)
        self.posts = defaultdict(deque)
        self.followees = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].appendleft((next(self.timer), tweetId))
        if len(self.posts[userId]) > 10:
            self.posts[userId].pop()

    def getNewsFeed(self, userId: int) -> list[int]:
        all_posts = heapq.merge(
            *(self.posts[uid] for uid in self.followees[userId] | {userId})
        )
        return [t_id for _, t_id in all_posts][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)
