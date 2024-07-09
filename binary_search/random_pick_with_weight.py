class Solution:
    def __init__(self, w: list[int]):
        self.weights = [(we, i) for i, we in enumerate(w)]
        self.weights.sort()
        self.n = len(self.weights)
        self.used = [0 for _ in range(self.n)]
        self.cur = 0

    def pickIndex(self) -> int:
        if self.used[0] == 0:
            self.used[0] += 1
            return self.weights[0][1]
        cur_ratio = self.used[self.cur] / self.used[0]
        if cur_ratio % self.weights[self.cur][0] == 0:
            self.cur = (self.cur + 1) % self.n
        self.used[self.cur] += 1
        return self.weights[self.cur][1]


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
