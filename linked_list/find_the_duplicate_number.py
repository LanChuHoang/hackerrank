# https://leetcode.com/problems/find-the-duplicate-number/


class Solution:
    def findDuplicate_v1(self, nums: list[int]) -> int:
        # Idea: Use the orginal array as a set to mark visited number
        # traverse the array, every time we visit a new number
        # mark it as visted number by changing the nums[i] = i
        # so that next time when we revisit it -> we can know it is the duplicated number

        i = 0
        while i < len(nums):
            if nums[i] == i:
                return nums[i]
            next_index = nums[i]
            nums[i] = i
            i = next_index

    def findDuplicate(self, nums: list[int]) -> int:
        # Idea: Use the Floyd's Tortoise and Hare algo to find the
        # duplicated number without changing the original array
        # - The first loop -> to find the meeting point in the circle
        # - The second loop -> to find the duplicated number

        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


print(Solution().findDuplicate([3, 1, 3, 4, 2]))
