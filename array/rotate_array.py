# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reduced_k = k % len(nums)
        if reduced_k == 0:
            return

        nums.reverse()

        for i in range(reduced_k // 2):
            nums[i], nums[reduced_k - 1 - i] = nums[reduced_k - 1 - i], nums[i]

        for i in range(reduced_k, reduced_k + (len(nums) - reduced_k) // 2):
            nums[i], nums[len(nums) - 1 - i + reduced_k] = (
                nums[len(nums) - 1 - i + reduced_k],
                nums[i],
            )

        # reduced_k = k % len(nums)
        # if reduced_k == len(nums):
        #     return

        # first_part = []
        # for i in range(reduced_k):
        #     first_part.append(nums[len(nums) - reduced_k + i])

        # second_part = []
        # for i in range(reduced_k, len(nums)):
        #     second_part.append(nums[i - reduced_k])

        # for i in range(len(first_part)):
        #     nums[i] = first_part[i]

        # for j in range(len(second_part)):
        #     i = j + reduced_k
        #     nums[i] = second_part[j]

        # print(first_part, second_part)
        # print(nums)


# Solution().rotate([1, 2, 3], 4)
