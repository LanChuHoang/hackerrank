# https://leetcode.com/problems/min-stack/

from collections import deque


class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()

    def set_min(self, val: int) -> None:
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
            return
        cur_min = min(val, self.min_stack[-1])
        self.min_stack.append(cur_min)

    def push(self, val: int) -> None:
        self.set_min(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
