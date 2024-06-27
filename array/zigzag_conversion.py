# https://leetcode.com/problems/zigzag-conversion/?envType=study-plan-v2&envId=top-interview-150

import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        result = []
        group_len = 2 * numRows - 2
        num_groups = math.ceil(len(s) / group_len)
        for r in range(numRows):
            for g in range(num_groups):
                first = g * group_len
                last = (g + 1) * group_len

                idx1 = first + r
                idx2 = last - r
                if idx1 < len(s):
                    result.append(s[idx1])
                if r != 0 and r != numRows - 1 and idx2 < len(s):
                    result.append(s[idx2])
        return "".join(result)


# s = Solution()
# print(s.convert("PAYPALISHIRING", 3))
