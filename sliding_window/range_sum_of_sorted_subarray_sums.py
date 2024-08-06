# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/description/?envType=daily-question&envId=2024-08-04

import heapq
from typing import List, Tuple


class Solution_v1:
    def rangeSum_v1(self, nums: list[int], n: int, left: int, right: int) -> int:
        # Idea: calculate all of subarray sums

        all_subarrs = []
        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum += nums[j]
                all_subarrs.append(cur_sum)
        all_subarrs.sort()
        print(all_subarrs)
        res = 0
        mod = 10**9 + 7
        for i in range(left - 1, right):
            res += all_subarrs[i] % mod
        return res % mod

    def rangeSum_v2(self, nums: list[int], n: int, left: int, right: int) -> int:
        # Idea: merge k sorted lists
        mod = 10**9 + 7
        pointers = []
        heap = []
        for i in range(n):
            pointers.append(i)
            heap.append((nums[i], i))
        heapq.heapify(heap)

        cur_len = 0
        res = 0
        while heap:
            min_sum, pointer_idx = heapq.heappop(heap)
            cur_len += 1
            if left <= cur_len <= right:
                res += min_sum % mod
            if cur_len > right:
                break
            if pointers[pointer_idx] + 1 < n:
                pointers[pointer_idx] += 1
                next_sum = min_sum + nums[pointers[pointer_idx]]
                heapq.heappush(heap, (next_sum, pointer_idx))
        return res % mod


class Solution:
    MODULUS = 10**9 + 7

    def count_and_sum_subarrays(
        self, array: List[int], threshold: int
    ) -> Tuple[int, int]:
        count, total_sum, running_sum, current_window_sum = 0, 0, 0, 0
        start = 0
        for end in range(len(array)):
            running_sum += (end - start + 1) * array[end]
            current_window_sum += array[end]
            while current_window_sum > threshold:
                running_sum -= current_window_sum
                current_window_sum -= array[start]
                start += 1
            total_sum += running_sum
            count += end - start + 1
        return count, total_sum

    def calculate_sum_of_first_k_subarrays(self, array: List[int], k: int) -> int:
        if k == 0:
            return 0
        low, high = min(array), sum(array)
        while low < high:
            mid = (low + high) // 2
            count, sum_value = self.count_and_sum_subarrays(array, mid)
            if count < k:
                low = mid + 1
            else:
                high = mid
        count, sum_value = self.count_and_sum_subarrays(array, high)
        return sum_value - (count - k) * high

    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        # Idea:
        # - using binary search to find to sum of first 'right' subarrays - s_right
        # and the first 'left - 1' subarrays - s_left
        # then result would be res = s_right - s_left
        # - to find the s_right and s_left
        #   + find the number of subarrays that sum <= subarrays[right - 1 / left - 2] and the
        # total sum of them
        #   + to find it, use binary search on the range [1, sum(nums)]
        #       + for each mid, we count all the subarrays that sum < mid
        #       + if count = right -> found
        #       + if the count > right -> decrease mid else increase mid

        # - technique to count the number of subarrays <= mid, and the sum of them
        # + in the expand phase: running_sum[end] = running_sum[end - 1]
        # + in the shrink phase: if the current_window_sum > target -> need to shrink the window
        # running_sum -= current_window_sum (because this window is invalid)
        # and current_window_sum -= nums[start]
        # + after the two phases: total_sum += running_sum
        # Explaination
        # - running_sum: is the total sum of all subarrays that end at the 'end' pointer and <= target
        result = self.calculate_sum_of_first_k_subarrays(
            nums, right
        ) - self.calculate_sum_of_first_k_subarrays(nums, left - 1)
        return result % self.MODULUS


s = Solution()
print(s.rangeSum(nums=[7, 5, 8, 5, 6, 4, 3, 3], n=8, left=2, right=6))
# print(s.rangeSum(nums=[1, 2, 3, 4], n=4, left=1, right=5))
print(s.rangeSum(nums=[1, 2, 3, 4], n=4, left=3, right=4))
# print(s.rangeSum(nums=[1, 2, 3, 4], n=4, left=1, right=10))
