# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        total_w = 0
        max_w = weights[0]
        for w in weights:
            total_w += w
            max_w = max(max_w, w)
        l, r = max_w, total_w
        res = total_w
        while l <= r:
            m = l + (r - l) // 2

            total_days = 0
            cur_sum = 0
            for w in weights:
                cur_sum += w
                if cur_sum > m:
                    total_days += 1
                    cur_sum = w
            total_days += 1
            is_valid = total_days <= days
            if is_valid:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res


s = Solution()
print(s.shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))
print(s.shipWithinDays(weights=[3, 2, 2, 4, 1, 4], days=3))
print(s.shipWithinDays(weights=[1, 2, 3, 1, 1], days=4))
