# https://leetcode.com/problems/count-number-of-teams/?envType=daily-question&envId=2024-07-29


class Solution:
    def numTeams(self, rating: list[int]) -> int:
        n = len(rating)
        num_largers = [0 for _ in range(n)]
        num_smallers = [0 for _ in range(n)]

        for i in range(n - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if rating[i] > rating[j]:
                    num_largers[j] += 1
                else:
                    num_smallers[j] += 1

        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if rating[i] < rating[j]:
                    res += num_largers[j]
                else:
                    res += num_smallers[j]

        return res


# s = Solution()
# print(s.numTeams(rating=[2, 5, 3, 4, 1]))
# print(s.numTeams(rating=[2, 1, 3]))
# print(s.numTeams(rating=[1, 2, 3, 4]))
