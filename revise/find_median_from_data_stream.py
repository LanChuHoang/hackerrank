# https://leetcode.com/problems/find-median-from-data-stream/

import heapq


class MedianFinder:
    def __init__(self):
        self.smaller_part = []
        self.larger_part = []

    def addNum(self, num: int) -> None:
        if not self.larger_part or (self.larger_part and num > self.larger_part[0]):
            heapq.heappush(self.larger_part, num)
        else:
            heapq.heappush(self.smaller_part, -num)

        l_len = len(self.larger_part)
        s_len = len(self.smaller_part)
        if l_len > s_len + 1:
            top = heapq.heappop(self.larger_part)
            heapq.heappush(self.smaller_part, -top)
        elif l_len < s_len:
            top = heapq.heappop(self.smaller_part)
            heapq.heappush(self.larger_part, -top)

    def findMedian(self) -> float:
        if (len(self.smaller_part) + len(self.larger_part)) % 2 == 0:
            return (-self.smaller_part[0] + self.larger_part[0]) / 2
        return self.larger_part[0]


s = MedianFinder()
s.addNum(1)
s.addNum(2)
print(s.findMedian())
s.addNum(3)
print(s.findMedian())
