# https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150

# We only need the left and right if the current element is larger than them
# So we first scan from left to right, if the current element is larger that the left,
# then we store the temp result. After that, we scan backward, and now we calculate
# actual result


from collections import defaultdict


class Solution:
    def candy_v1(self, ratings: list[int]) -> int:
        result = [0] * len(ratings)
        frequency = defaultdict(list)
        for i in range(len(ratings)):
            frequency[ratings[i]].append(i)

        total_candies = 0
        for r in sorted(frequency.keys()):
            for i in frequency[r]:
                num_candies = 1
                if i - 1 >= 0 and ratings[i] > ratings[i - 1]:
                    num_candies = result[i - 1] + 1
                if i + 1 < len(ratings) and ratings[i] > ratings[i + 1]:
                    num_candies = max(num_candies, result[i + 1] + 1)
                total_candies += num_candies
                result[i] = num_candies

        return total_candies

    def candy_v2(self, ratings: list[int]) -> int:
        result = [0] * len(ratings)
        total = 0

        def dfs(i: int):
            nonlocal total

            if result[i] != 0:
                return result[i]

            num_candies = 1
            if i - 1 >= 0 and ratings[i] > ratings[i - 1]:
                num_candies = dfs(i - 1) + 1
            if i + 1 < len(ratings) and ratings[i] > ratings[i + 1]:
                num_candies = max(num_candies, dfs(i + 1) + 1)

            result[i] = num_candies
            total += num_candies
            return result[i]

        for i in range(len(ratings)):
            dfs(i)
        return total

    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1

        result = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                result[i] = result[i - 1] + 1

        total = result[-1]
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                result[i] = max(result[i], result[i + 1] + 1)
            total += result[i]
        # print(result)
        return total


# s = Solution()

# print(s.candy([1, 0, 2]))
