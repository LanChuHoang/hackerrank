# https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        total_len = len_nums1 + len_nums2
        half = total_len // 2
        A, B = (nums1, nums2) if len_nums1 < len_nums2 else (nums2, nums1)

        i, j = 0, len(A) - 1

        while True:
            m = (i + j) // 2

            a_left_most_idx = m
            b_left_most_idx = half - (a_left_most_idx + 1) - 1
            a_right_most_idx = a_left_most_idx + 1
            b_right_most_idx = b_left_most_idx + 1

            a_left_most = A[a_left_most_idx] if a_left_most_idx >= 0 else float("-inf")
            b_left_most = B[b_left_most_idx] if b_left_most_idx >= 0 else float("-inf")
            a_right_most = (
                A[a_right_most_idx] if a_right_most_idx < len(A) else float("inf")
            )
            b_right_most = (
                B[b_right_most_idx] if b_right_most_idx < len(B) else float("inf")
            )

            merged_left_most = max(a_left_most, b_left_most)
            merged_right_most = min(a_right_most, b_right_most)
            # Correct
            if merged_left_most <= merged_right_most:
                return (
                    merged_right_most
                    if total_len % 2 != 0
                    else (merged_left_most + merged_right_most) / 2
                )
            elif b_left_most > merged_right_most:
                i = m + 1
            else:
                j = m - 1
