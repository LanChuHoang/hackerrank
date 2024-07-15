# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/


class Solution:
    def count_num_bouquets(self, bloom_day: list[int], k: int, num_days: int) -> int:
        total = 0
        cur_consecutive = 0
        for b_day in bloom_day:
            if b_day <= num_days:
                cur_consecutive += 1
                if cur_consecutive == k:
                    total += 1
                    cur_consecutive = 0
            else:
                cur_consecutive = 0
        return total

    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        l, r = min(bloomDay), max(bloomDay)
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            num_bouquets = self.count_num_bouquets(bloomDay, k, mid)
            if num_bouquets >= m:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


# s = Solution()
# print(s.minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=1))
# print(s.minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=2))
# print(s.minDays(bloomDay=[7, 7, 7, 7, 12, 7, 7], m=2, k=3))
