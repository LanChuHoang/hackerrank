from collections import Counter


class Solution:
    def minimumPushes_v1(self, word: str) -> int:
        counter = Counter(word)
        sorted_frequency = sorted(counter.values(), reverse=True)

        nums = [[] for _ in range(8)]
        for i in range(len(sorted_frequency)):
            group = i // 8
            if group % 2 == 0:
                j = i % 8
            else:
                j = 7 - (i % 8)
            nums[j].append(sorted_frequency[i])
        res = 0
        for n in nums:
            for i in range(len(n)):
                res += (i + 1) * n[i]
        return res

    def minimumPushes(self, word: str) -> int:
        # Idea: count the freq of each character
        # try to balance the distribution of chars

        counter = Counter(word)
        sorted_frequency = sorted(counter.values(), reverse=True)

        res = 0
        for i in range(len(sorted_frequency)):
            group = i // 8
            res += sorted_frequency[i] * (group + 1)
        return res


s = Solution()

print(s.minimumPushes("abcde"))
print(s.minimumPushes("xyzxyzxyzxyz"))
print(s.minimumPushes("aabbccddeeffgghhiiiiii"))
# print(s.minimumPushes())
