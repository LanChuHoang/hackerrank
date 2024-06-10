# https://leetcode.com/problems/longest-increasing-subsequence/description/


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        last_idx = []
        for i in range(len(nums)):
            # Check if the current element can expand the current longest increase subsequence
            # If can expand -> store the current idx as the last idx of the new lis
            # If not -> replace the curren idx with the appropriate increase subsequence to maximize the
            # probability to create new lis in the future

            if not last_idx or nums[i] > nums[last_idx[-1]]:
                last_idx.append(i)
            else:
                # do b-search to find the smallest larger element
                to_find_idx = 0
                l, r = 0, len(last_idx) - 1
                while l <= r:
                    m = (l + r) // 2
                    mid_num = nums[last_idx[m]]
                    if mid_num < nums[i]:
                        l = m + 1
                    else:
                        r = m - 1
                        to_find_idx = m
                last_idx[to_find_idx] = i
        return len(last_idx)


# solution = Solution()
# print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
# print(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))
# print(solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
