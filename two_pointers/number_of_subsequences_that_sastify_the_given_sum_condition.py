# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/?envType=study-plan-v2&envId=binary-search


class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        """
        Idea 1: subsequence 2, 1, 4, 3 and 1, 2, 3, 4 have the same max and length -> sort
        Idea 2: the problem now is find a pair that sum <= target -> 2 pointers
        Idea 3: for a given pair of i, j like
            - 1, 2, 3, 4, 5, 6; (i, j) = (0, 5); target = 7
            - number of subs that sum(min, max) <= target is
                - min, max = 1, 6 -> 2^4 (from 2 to 5 pick any subset)
                - 1, 5 -> 2^3
                - 1, 4 -> 2^2
                - 1, 3 -> 2^1
                - 1, 2 -> 2^0
                - 1, 1 -> 1

        -> S = 1 + sum(2^x) (x in [0, j - i - 1]) = 1 + 1*(2^(j - i - 1) - 1)/1 = 2^(j-i)
        Idea 4: use `pow()` for calculate 2^n % m
        """
        nums.sort()
        n = len(nums)
        l, r = 0, n - 1
        res = 0
        mod = 10**9 + 7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, mod)
                l += 1
        return res


# s = Solution()
# print(s.numSubseq(nums=[3, 5, 6, 7], target=9))
# print(s.numSubseq(nums=[3, 3, 6, 8], target=10))
# print(s.numSubseq(nums=[2, 3, 3, 4, 6, 7], target=12))
