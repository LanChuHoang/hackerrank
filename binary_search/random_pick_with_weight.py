import random


class Solution:
    def __init__(self, weights: list[int]):
        self.cdf = [0]
        for w in weights:
            self.cdf.append(self.cdf[-1] + w)

    def pickIndex(self) -> int:
        # Idea: create a cdf array: cumulative distribution function or simply a prefix sum
        # [0, a0, a1 + a0, a2 + a1 + a0 ...]
        # then generate a random number from [1, sum(all elements)]
        # and find the smallest element in the array that >= rand_num
        # so the probability of getting a0 is # of [1, ... a0] / # of [1,...,sum(all)] = a0/sum(all)
        # a1: # of [a0 + 1, a0 + 2,..., a1 + a0] / # of [1,...,sum(all)] = a1 / sum(all)
        # ... and so on
        rand_num = random.randint(1, self.cdf[-1])
        l, r = 1, len(self.cdf) - 1
        while l < r:
            m = l + (r - l) // 2
            if self.cdf[m] >= rand_num:
                r = m
            else:
                l = m + 1
        return l - 1


nums = [10, 7, 8, 10]
obj = Solution(nums)
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())

print(obj.pickIndex())


# for num, org_i in sorted([(n, i) for i, n in enumerate(nums)]):
#     for _ in range(num):
#         res = obj.pickIndex()
#         if res != org_i:
#             print(res, org_i, num)
# # print(obj.pickIndex())
# # print(obj.pickIndex())
# # print(obj.pickIndex())
# # print(obj.pickIndex())
