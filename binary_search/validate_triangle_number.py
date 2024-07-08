# https://leetcode.com/problems/valid-triangle-number/?envType=study-plan-v2&envId=binary-search


class Solution:
    def triangleNumber_v1(self, nums: list[int]) -> int:
        # Idea: fixed a, b, find the greatest c so that (a + b) > c and a <= c, b <= c
        # Complexity: O(n^2*log(n))
        nums = sorted(filter(lambda x: x != 0, nums))
        n = len(nums)
        if n < 3:
            return 0
        result = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                largest_c_idx = None
                l, r = j + 1, n - 1
                while l <= r:
                    m = l + (r - l) // 2
                    if nums[m] < nums[i] + nums[j]:
                        largest_c_idx = m
                        l = m + 1
                    else:
                        r = m - 1
                if largest_c_idx is not None:
                    result += largest_c_idx - j

        return result

    def triangleNumber(self, nums: list[int]) -> int:
        # Idea: Fixed c
        # 2 pointers for i, j = 0, k - 1 or a and b
        # for each iteration:
        # if a + b > c then there are j - 1 - i + 1 = j - i pairs that a + b > c
        # then result += j - i, j -= 1 for other b
        # else
        # increase a so a + b can > c
        nums.sort()
        n = len(nums)
        if n < 3:
            return 0
        result = 0
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    result += j - i
                    j -= 1
                else:
                    i += 1

        return result


# s = Solution()
# print(s.triangleNumber([2, 2, 3, 4]))
# print(s.triangleNumber([4, 2, 3, 4]))
# print(s.triangleNumber([4]))
# print(s.triangleNumber([0, 0, 0, 0]))
