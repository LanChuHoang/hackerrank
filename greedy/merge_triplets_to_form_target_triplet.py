# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/


class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        found_index = set()

        for triplet in triplets:
            if (
                triplet[0] > target[0]
                or triplet[1] > target[1]
                or triplet[2] > target[2]
            ):
                continue

            for i, value in enumerate(triplet):
                if value == target[i]:
                    found_index.add(i)

            if len(found_index) == 3:
                return True

        return False
