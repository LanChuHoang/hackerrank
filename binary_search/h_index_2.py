# https://leetcode.com/problems/h-index-ii/?envType=study-plan-v2&envId=binary-search


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        if citations[-1] == 0:
            return 0

        n = len(citations)
        l, r = 1, n

        result = n
        while l <= r:
            m = l + (r - l) // 2
            smallest_el = citations[n - m]
            if m == smallest_el:
                result = m
                break
            elif m < smallest_el:
                result = m
                l = m + 1
            else:
                r = m - 1

        return result
