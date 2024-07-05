# https://leetcode.com/problems/find-right-interval/?envType=study-plan-v2&envId=binary-search


class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        sorted_starts = [(start, i) for i, (start, _) in enumerate(intervals)]
        sorted_starts.sort()
        result = [-1 for _ in range(n)]
        for i, (start, end) in enumerate(intervals):
            if start >= end:
                result[i] = i
            else:
                l, r = 0, n - 1
                while l <= r:
                    m = (l + r) // 2
                    if end == sorted_starts[m][0]:
                        result[i] = sorted_starts[m][1]
                        break
                    elif end < sorted_starts[m][0]:
                        result[i] = sorted_starts[m][1]
                        r = m - 1
                    else:
                        l = m + 1
        return result


# s = Solution()

# print(s.findRightInterval([[1, 2]]))
# print(s.findRightInterval([[3, 4], [2, 3], [1, 2]]))
# print(s.findRightInterval([[1, 4], [2, 3], [3, 4]]))
