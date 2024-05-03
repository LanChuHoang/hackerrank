# https://leetcode.com/problems/partition-labels/description/


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_idx = dict()
        for i, c in enumerate(s):
            last_idx[c] = i

        total_size = 0
        result = []
        can_stop_idx = -1
        for i, c in enumerate(s):
            can_stop_idx = max(can_stop_idx, last_idx[c])
            if i == can_stop_idx:
                size = can_stop_idx + 1 - total_size
                result.append(size)
                can_stop_idx = -1
                total_size += size

        return result


# print(Solution().partitionLabels("e"))
