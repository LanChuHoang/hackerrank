# https://leetcode.com/problems/binary-search/

class Solution:
    def binary_search(self, nums: list[int], left: int, right: int, target: int) -> int:
        if left > right:
            return -1
        
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary_search(nums, mid + 1, right, target)
        else:
            return self.binary_search(nums, left, mid - 1, target)

    def search(self, nums: list[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)
    
solution = Solution()
print(solution.search([-1,0,3,5,9,12], 2))