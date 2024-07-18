# https://leetcode.com/problems/sliding-window-maximum/

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # Idea: Maintain a non-increasing stack
        # - every time the window pop the left element, we can check the
        # the stack to see whether it is the maximum, if it is -> pop the stack
        # left, then the next maximum will be the next element in the stack
        # - every time the window push the right element, we insert it the the
        # stack to create a non-increasing stack, so in the next popping phase
        # the can get the next maximum
        if len(nums) <= 1:
            return nums
        start, end = 0, k - 1
        result = []
        stack = deque()
        for i in range(start, end + 1, 1):
            while stack and stack[-1] < nums[i]:
                stack.pop()
            stack.append(nums[i])
        result.append(stack[0])

        while True:
            # print(nums[start : end + 1], stack, result)
            if nums[start] == stack[0]:
                stack.popleft()
            start += 1

            end += 1
            if end >= len(nums):
                break
            while stack and stack[-1] < nums[end]:
                stack.pop()
            stack.append(nums[end])

            result.append(stack[0])

        return result


# print(Solution().maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
