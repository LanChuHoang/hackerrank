# https://leetcode.com/problems/find-the-duplicate-number/description/


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
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


# s = Solution()
# print(s.findDuplicate([1, 3, 4, 2, 2]))
