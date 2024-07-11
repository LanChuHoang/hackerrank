# https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/description/


"""
This is the custom function interface.
You should not implement it, or speculate about its implementation
class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
"""


class Solution(object):
    def findSolution_v1(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        res = []
        for x in range(1, 1001):
            l, r = 1, 1000
            while l <= r:
                m = l + (r - l) // 2
                cur_z = customfunction(x, m)
                if cur_z == z:
                    res.append([x, m])
                    break
                elif cur_z < z:
                    l = m + 1
                else:
                    r = m - 1
        return res

    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        res = []
        x, y = 1, 1000
        while x <= 1000 and y >= 1:
            s = customfunction.f(x, y)
            if s == z:
                res.append([x, y])
                x += 1
                y -= 1
            elif s < z:
                x += 1
            else:
                y -= 1
        return res
