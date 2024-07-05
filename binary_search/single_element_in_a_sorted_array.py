# https://leetcode.com/problems/single-element-in-a-sorted-array/description/?envType=study-plan-v2&envId=binary-search


class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        l, r = 0, n - 1
        while l <= r:
            m = l + (r - l) // 2

            if m == 0:
                if nums[m] != nums[m + 1]:
                    return nums[m]
                else:
                    l = m + 2
            if m == n - 1:
                if nums[m] != nums[m - 1]:
                    return nums[m]
                else:
                    r = m - 2
            if nums[m] != nums[m + 1] and nums[m] != nums[m - 1]:
                return nums[m]
            elif nums[m] == nums[m + 1]:
                if (n - m) % 2 == 0:
                    r = m - 1
                else:
                    l = m + 2
            else:
                if (n - m + 1) % 2 == 0:
                    r = m - 1
                else:
                    l = m + 1


# s = Solution()
# print(s.singleNonDuplicate(nums=[1, 1, 2, 2, 3]))
