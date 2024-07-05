# https://leetcode.com/problems/find-k-closest-elements/description/?envType=study-plan-v2&envId=binary-search


class Solution:
    # def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
    #     n = len(arr)
    #     l, r = 0, n - 1
    #     closest_idx = 0
    #     closest_dis = abs(arr[0] - x)
    #     while l <= r:
    #         m = l + (r - l) // 2
    #         if arr[m] == x:
    #             closest_idx = m
    #             closest_dis = 0
    #             break
    #         elif arr[m] > x:
    #             dis = arr[m] - x
    #             r = m - 1
    #         else:
    #             dis = x - arr[m]
    #             l = m + 1
    #         if dis < closest_dis or dis == closest_dis and arr[m] < arr[closest_idx]:
    #             closest_idx = m
    #             closest_dis = dis

    #     left_els = []
    #     right_els = []
    #     l, r = closest_idx - 1, closest_idx + 1
    #     while len(left_els) + len(right_els) + 1 < k:
    #         if l >= 0 and r < n:
    #             if abs(arr[l] - x) <= abs(arr[r] - x):
    #                 left_els.append(arr[l])
    #                 l -= 1
    #             else:
    #                 right_els.append(arr[r])
    #                 r += 1
    #         elif l >= 0:
    #             left_els.append(arr[l])
    #             l -= 1
    #         else:
    #             right_els.append(arr[r])
    #             r += 1
    #     return list(reversed(left_els)) + [arr[closest_idx]] + right_els

    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        n = len(arr)
        l, r = 0, n - k
        while l < r:
            m = l + (r - l) // 2
            if x - arr[m] <= arr[m + k] - x:
                r = m
            else:
                l = m + 1
        return arr[l : l + k]


# s = Solution()
# print(s.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3))
# print(s.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=-1))
# print(s.findClosestElements(arr=[1, 2, 6, 7, 8], k=4, x=3))
# print(s.findClosestElements(arr=[1, 2, 6, 7, 8], k=4, x=5))
