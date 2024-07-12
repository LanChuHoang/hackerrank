# https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/solutions/

import math


class Solution:
    def maximumGroups(self, grades: list[int]) -> int:
        # Idea 1: to maximize the number of groups, we can store it like this
        # group 1: 1 el
        # group 2: 2 els
        # ..
        # group x: all of the last elements
        # the elements are inserted in ascending order to ensure group i + 1 > group i
        # Idea 2: the perfect case is we can form groups like this
        # 1, 2, ..., n where (1 + x)*x = n
        # but if there are extra elements that not enough to form a new x then we can store
        # all of those in the last group
        # Idea 3: so the problem now is find the max x that S=(1+x)*x <= n
        # we solve the equation (1+x)*x = n and get floor part of x
        # The fomular of x is x = (1 + sqrt(1 + 8*n)) / 2

        n = len(grades)
        x = math.floor((-1 + math.sqrt(1 + 8 * n)) / 2)
        return x
