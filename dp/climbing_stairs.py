# https://leetcode.com/problems/climbing-stairs/


"""
x: is the target sum
so number of possible combinations n(x) = n(x - 1) + n(x - 2)
because the number of combinations for x is the total of the number of combination if we put 1 to the combination n(x - 1)
and put 2 to the combination n(x - 2)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        num_if_take_1 = 1
        num_if_take_2 = 1
        for _ in range(2, n + 1):
            cur_num = num_if_take_1 + num_if_take_2
            num_if_take_1 = num_if_take_2
            num_if_take_2 = cur_num
        return cur_num


# print(Solution().climbStairs(5))
