# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
