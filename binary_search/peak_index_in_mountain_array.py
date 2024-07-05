# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/?envType=study-plan-v2&envId=binary-search


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        n = len(arr)
        if n == 3:
            return arr[1]
        l, r = 1, n - 2
        while l <= r:
            m = l + (r - l) // 2
            if arr[m - 1] < arr[m] > arr[m + 1]:
                return m
            elif arr[m - 1] >= arr[m]:
                r = m - 1
            else:
                l = m + 1


# s = Solution()
# print(s.peakIndexInMountainArray([0, 2, 1, 0]))
