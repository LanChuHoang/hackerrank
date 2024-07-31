# https://leetcode.com/problems/task-scheduler/description/

import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        heap = []
        counter = dict()
        for t in tasks:
            counter[t] = counter.get(t, 0) + 1
        for c in counter.values():
            heapq.heappush(heap, (0, -c))

        i = 0
        while heap:
            top_task = heapq.heappop(heap)
            next_idx, num_remain = top_task

            next_i = max(i, next_idx)
            next_idx = i + n + 1
            num_remain += 1
            if num_remain != 0:
                heapq.heappush(heap, (next_idx, num_remain))
            i = next_i
        return i + 1


s = Solution()
print(s.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2))
print(s.leastInterval(tasks=["A", "C", "A", "B", "D", "B"], n=1))
print(s.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=3))
