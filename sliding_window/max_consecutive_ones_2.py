# https://leetcode.com/problems/max-consecutive-ones-iii/description/


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        count = 1 if nums[0] == 1 else 0
        n = len(nums)
        l, r = 0, 0
        res = 0
        while l < n and r < n:
            w_len = r - l + 1
            num_changes = w_len - count

            if num_changes <= k:
                res = max(res, w_len)
                r += 1
                if r < n and nums[r] == 1:
                    count += 1
            else:
                if nums[l] == 1:
                    count -= 1
                l += 1
        return res


# s = Solution()
# print(s.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
# print(
#     s.longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3)
# )
