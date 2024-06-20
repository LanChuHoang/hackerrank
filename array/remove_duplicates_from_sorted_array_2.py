# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Idea: maintain 2 pointers, the first one is to keep track the last position
        # of the new array for inserting elements. The second is to count the number of
        # duplicates for each element in the old array and use it to insert to the
        # new array via the first pointer
        i, j = 0, 0
        while j < len(nums):
            num_dups = 0
            cur_num = nums[j]
            while j < len(nums) and nums[j] == cur_num:
                num_dups += 1
                j += 1

            if num_dups >= 2:
                nums[i] = cur_num
                nums[i + 1] = cur_num
                i += 2
            else:
                nums[i] = cur_num
                i += 1
        return i
