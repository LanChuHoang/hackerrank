# https://leetcode.com/problems/russian-doll-envelopes/?envType=study-plan-v2&envId=binary-search

import bisect


class Solution:
    def maxEnvelopes_v1(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # print(envelopes)

        # lis
        n = len(envelopes)
        lis = [0 for _ in range(n)]
        j = 0
        for i in range(1, n):
            if envelopes[i][1] > envelopes[lis[j]][1]:
                j += 1
                lis[j] = i
            else:
                l, r = 0, j
                while l < r:
                    m = l + (r - l) // 2
                    if envelopes[lis[m]][1] >= envelopes[i][1]:
                        r = m
                    else:
                        l = m + 1
                lis[l] = i
        return j + 1

    def len_of_lis(self, arr: list[int]) -> int:
        dp = []
        for num in arr:
            j = bisect.bisect_left(dp, num)
            if j == len(dp):
                dp.append(num)
            else:
                dp[j] = num
        return len(dp)

    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [e[1] for e in envelopes]
        return self.len_of_lis(heights)


# s = Solution()
# print(s.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))
# print(s.maxEnvelopes([[1, 1], [1, 1], [1, 1]]))
# print(s.maxEnvelopes([[4, 5], [4, 6], [6, 7], [2, 3], [1, 1], [1, 1]]))
# print(
#     s.maxEnvelopes(
#         [[1, 2], [2, 3], [3, 5], [3, 4], [4, 5], [5, 6], [5, 5], [6, 7], [7, 8]]
#     )
# )
