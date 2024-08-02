# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/?envType=daily-question&envId=2024-08-02


class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        # Idea:
        # find the minimum window which contains the minimum of 0
        # because it requires the least number of swaps to correct

        win_len = 0
        for n in nums:
            if n == 1:
                win_len += 1
        n = len(nums)
        res = win_len
        need = 0
        l, r = 0, 0
        while r < win_len:
            if nums[r] == 0:
                need += 1
            r += 1
        res = min(res, need)
        r -= 1
        for l in range(1, n):
            prev_l = l - 1
            if nums[prev_l] == 0:
                need -= 1
            r = (r + 1) % n
            if nums[r] == 0:
                need += 1
            res = min(res, need)

        return res


s = Solution()
print(s.minSwaps(nums=[0, 1, 0, 1, 1, 0, 0]))
print(s.minSwaps(nums=[0, 1, 1, 1, 0, 0, 1, 1, 0]))
print(s.minSwaps(nums=[1, 1, 0, 0, 1]))
