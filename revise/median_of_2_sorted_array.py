# https://leetcode.com/problems/median-of-two-sorted-arrays/description/


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        nums1_len = len(nums1)
        nums2_len = len(nums2)
        overall_half = (nums1_len + nums2_len) // 2
        if nums2_len == 0:
            return (
                nums1[overall_half]
                if nums1_len % 2 != 0
                else (nums1[overall_half - 1] + nums1[overall_half]) / 2
            )

        l, r = 0, nums2_len - 1
        while l <= r:
            m2 = (l + r) // 2
            m1 = overall_half - m2 - 2

            a1 = nums1[m1] if m1 >= 0 else None
            b1 = nums1[m1 + 1] if m1 + 1 < nums1_len else None

            a2 = nums2[m2]
            b2 = nums2[m2 + 1] if m2 + 1 < nums2_len else None

            if b1 is not None and a2 > b1:
                r = m2 - 1
            elif b2 is not None and a1 > b2:
                l = m2 + 1
            else:
                max_a = max(a1, a2) if a1 is not None else a2
                min_b = min(b1, b2) if b2 is not None else b1
                return (
                    min_b if (nums1_len + nums2_len) % 2 != 0 else (max_a + min_b) / 2
                )
        max_a = nums1[overall_half - 1]
        min_b = (
            min(nums1[overall_half], nums2[0]) if overall_half < nums1_len else nums2[0]
        )
        return min_b if (nums1_len + nums2_len) % 2 != 0 else (max_a + min_b) / 2


s = Solution()
# print(s.findMedianSortedArrays([1, 3], [2]))
# print(s.findMedianSortedArrays([1, 2], [3, 4]))
# print(s.findMedianSortedArrays([3, 4], [1, 2]))
# print(s.findMedianSortedArrays([1], []))
