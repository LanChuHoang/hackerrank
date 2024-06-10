# https://leetcode.com/problems/partition-equal-subset-sum/description/


class Solution:
    def canPartition_v1(self, nums: list[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        targeted_sum = total_sum // 2
        dp_table = [
            [False for _ in range(targeted_sum + 1)] for _ in range(len(nums) + 1)
        ]
        dp_table[0][0] = True
        for num_elements in range(1, len(nums) + 1):
            cur_element = nums[num_elements - 1]
            for target in range(targeted_sum + 1):
                is_already_makable = dp_table[num_elements - 1][target]
                is_now_makable = (
                    target - cur_element >= 0
                    and dp_table[num_elements - 1][target - cur_element]
                )
                is_makable = is_already_makable or is_now_makable
                dp_table[num_elements][target] = is_makable
                if target == targeted_sum and is_makable:
                    return True

        return False

    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        targeted_sum = total_sum // 2
        makable_sums = set()
        makable_sums.add(0)
        for num_elements in range(1, len(nums) + 1):
            cur_element = nums[num_elements - 1]

            now_makable_sums = set()
            for prev_makable_sum in makable_sums:
                now_makable_sum = prev_makable_sum + cur_element

                if now_makable_sum == targeted_sum:
                    return True

                if now_makable_sum < targeted_sum:
                    now_makable_sums.add(now_makable_sum)

            makable_sums.update(now_makable_sums)

        return False


# solution = Solution()
# print(solution.canPartition([1, 5, 11, 5]))
# print(solution.canPartition([1, 2, 5]))
