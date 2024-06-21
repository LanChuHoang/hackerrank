# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
            return

        p1, p2 = m - 1, n - 1
        while p1 >= 0 and p2 >= 0:
            k = p1 + p2 + 1
            if nums1[p1] > nums2[p2]:
                nums1[k] = nums1[p1]
                p1 -= 1
            else:
                nums1[k] = nums2[p2]
                p2 -= 1

        while p2 >= 0:
            nums1[p2] = nums2[p2]
            p2 -= 1
