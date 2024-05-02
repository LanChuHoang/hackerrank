# https://leetcode.com/problems/task-scheduler/description/

import heapq
from collections import deque, Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # Init a priority queue based on the number of tasks to select the highest priority task to execute
        # the task with the most frequency should be execute first for idle time reduction
        frequency = Counter(tasks)
        priority_queue = [f * -1 for f in frequency.values()]
        heapq.heapify(priority_queue)

        # Every time we execute a task, we need to store the remaining tasks and the available time to
        # the queue for execution
        waiting_queue = deque()

        # For each loop
        # 1. check the waiting queue for the task that done waiting, -> add to the priority queue
        # 2. get the max priority task from the priority queue, execute this task, if there are more tasks like this task
        # calculate the available time, add those to the waiting queue
        # 3. increase the time until no task left in both queues

        t = 0
        while priority_queue or waiting_queue:
            if waiting_queue and waiting_queue[0][1] == t:
                done_waiting_task = waiting_queue.popleft()
                heapq.heappush(priority_queue, done_waiting_task[0])
            if priority_queue:
                max_priority_task_count = heapq.heappop(priority_queue)
                # +1 because the frequency is neg to implement max heap in python
                num_tasks_left = max_priority_task_count + 1
                if num_tasks_left != 0:
                    # +1 for the current task execution time
                    next_avail_time = t + 1 + n
                    waiting_queue.append((num_tasks_left, next_avail_time))

            t += 1
        return t
