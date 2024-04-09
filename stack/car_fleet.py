# https://leetcode.com/problems/car-fleet/description/

from collections import deque


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = deque()
        result = 0
        pos_time_list = sorted(
            [
                (position[i], (target - position[i]) / speed[i])
                for i in range(len(position))
            ],
            reverse=True,
        )
        for _, time in pos_time_list:
            has_car_fleet = False
            while stack and stack[0] < time:
                has_car_fleet = True
                stack.pop()
            if has_car_fleet:
                result += 1
            stack.append(time)

        if stack:
            result += 1
        return result


print(Solution().carFleet(target=10, position=[0, 4, 2], speed=[2, 1, 3]))
