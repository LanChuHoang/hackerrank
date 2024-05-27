# https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Run binary search on the shorter array
        For each loop:
        1. Find the left haft of the shorter array
        2. Find the missing part in the longer array to create a valid merged left half
        - The left most of the shorter array is the last idx of the left half in the shorter array
        - The left most of the longer array is the last idx of the missing part of the longer array
        - The missing part is created from the longer array from 0 to n, such at
        length + the length of the left haft part of the shorter array = total length // 2
        3. Check if the left most of the shorter array < the right most of the longer array
        and the left most of the longer array < the right most of the shorter array
        --> the merged left half is valid
        --> return either the merged right most
        if the total length is a odd number of avg of merged left most and merged right most
        4. If it not valid -> find the next mid point in the shorter array until valid
        - If the left most of the longer array > the right most of the shorter array
        --> increase mid to reduce the left most of the longer array
        - If the left most of the shorter array > the right most of the longer array
        --> decrease mid to reduce the left most of the shorter array
        """
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
