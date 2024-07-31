# https://leetcode.com/problems/task-scheduler/description/

import heapq
from collections import deque, Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        frequency = Counter(tasks)
        ready_queue = [-f for f in frequency.values()]
        heapq.heapify(ready_queue)
        waiting_queue = deque()

        t = 0
        while waiting_queue or ready_queue:
            if waiting_queue and waiting_queue[0][0] == t:
                ready_task = waiting_queue.popleft()
                heapq.heappush(ready_queue, ready_task[1])
            if ready_queue:
                num_tasks_left = heapq.heappop(ready_queue)
                num_tasks_left += 1
                if num_tasks_left != 0:
                    available_t = t + n + 1
                    waiting_queue.append((available_t, num_tasks_left))
            t += 1
        return t


s = Solution()
print(
    s.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=1)
)
print(s.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2))
print(s.leastInterval(tasks=["A", "C", "A", "B", "D", "B"], n=1))
print(s.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=3))
