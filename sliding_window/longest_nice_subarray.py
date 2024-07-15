# https://leetcode.com/problems/longest-nice-subarray/description/


class Solution:
    def brute_force(self, nums: list[int]):
        l, r = 0, 1
        res_l, res_r = l, l
        n = len(nums)
        while r < n:
            is_valid = True
            for i in range(l, r):
                if nums[i] & nums[r] != 0:
                    is_valid = False
                    break
            if is_valid:
                if r - l > res_r - res_l:
                    res_l, res_r = l, r
                r += 1
            else:
                l += 1
        return nums[res_l : res_r + 1]

    def longestNiceSubarray(self, nums: list[int]) -> int:
        res = 0
        xor_sofar = 0
        l, r = 0, 0
        n = len(nums)
        while l < n and r < n:
            if xor_sofar & nums[r] == 0:
                res = max(res, r - l + 1)
                xor_sofar ^= nums[r]
                r += 1
            else:
                xor_sofar ^= nums[l]
                l += 1
        return res


# s = Solution()
# print(s.longestNiceSubarray(nums=[1, 3, 8, 48, 10]))
# print(s.longestNiceSubarray(nums=[3, 1, 5, 11, 13]))
# print(
#     s.longestNiceSubarray(
#         [
#             84139415,
#             693324769,
#             614626365,
#             497710833,
#             615598711,
#             264,
#             65552,
#             50331652,
#             1,
#             1048576,
#             16384,
#             544,
#             270532608,
#             151813349,
#             221976871,
#             678178917,
#             845710321,
#             751376227,
#             331656525,
#             739558112,
#             267703680,
#         ]
#     )
# )
