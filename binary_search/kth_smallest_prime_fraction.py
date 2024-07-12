# https://leetcode.com/problems/k-th-smallest-prime-fraction/submissions/1318119288/

import heapq


class Solution:
    def kthSmallestPrimeFraction_v1(self, arr: list[int], k: int) -> list[int]:
        # Idea: list every f, and push to a max_heap of size k
        heap_arr = []

        n = len(arr)
        for i in range(n - 1):
            for j in range(i + 1, n):
                f = arr[i] / arr[j]
                if len(heap_arr) < k:
                    heapq.heappush(heap_arr, (-f, i, j))
                else:
                    heapq.heappushpop(heap_arr, (-f, i, j))
        _, i, j = heapq.heappop(heap_arr)
        return arr[i], arr[j]

    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        # Idea: bsearch in range (0, 1)
        # - For each check the total number of elements that smaller than mid
        # - If total == k: return the max of them
        # Idea 2: for checking in O(2n)
        # - Iterate i from (0, n-1)
        # - for each loop, dont reset j to i+1, because every i+1/k for k in [0, j - 1]
        # is already >= mid
        # So the total number of works is 2n
        n = len(arr)
        l, r = 0, 1.0
        while l < r:
            m = (l + r) / 2

            total = 0
            j = 1
            max_smaller_than_m = 0
            num, dem = 0, 0
            for i in range(n - 1):
                while j < n and arr[i] >= arr[j] * m:
                    j += 1

                num_smaller_than_m = n - j
                total += num_smaller_than_m

                if j == n:
                    break

                f = arr[i] / arr[j]
                if f > max_smaller_than_m:
                    max_smaller_than_m = f
                    num = arr[i]
                    dem = arr[j]

            if total == k:
                return num, dem
            elif total > k:
                r = m
            else:
                l = m


# s = Solution()
# print(s.kthSmallestPrimeFraction(arr=[1, 2, 3, 5], k=3))
# print(s.kthSmallestPrimeFraction(arr=[1, 7], k=1))
