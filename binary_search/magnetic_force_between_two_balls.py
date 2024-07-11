# https://leetcode.com/problems/magnetic-force-between-two-balls/description/


class Solution:
    def check_valid(self, position: list[int], nums: int, min_dis: int) -> bool:
        prev_pos = 0
        num_pos = 1
        for i in range(1, len(position)):
            if position[i] - position[prev_pos] >= min_dis:
                num_pos += 1
                prev_pos = i
            if num_pos == nums:
                return True
        return False

    def maxDistance(self, position: list[int], nums: int) -> int:
        # Idea: binary search on the result range
        # for each result check to verify whether we can form a solution or not
        # if yes, try to increase the result
        # if not, decrease the result

        position.sort()
        l, r = 1, (position[-1] - position[0]) // (nums - 1)

        res = 0
        while l <= r:
            m = l + (r - l) // 2

            is_valid = self.check_valid(position, nums, m)
            if is_valid:
                l = m + 1
                res = m
            else:
                r = m - 1

        return res


# s = Solution()
# print(s.maxDistance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
# print(s.maxDistance([5, 4, 3, 2, 1, 1000000000], 2))
# print(s.maxDistance([79, 74, 57, 22], 4))
