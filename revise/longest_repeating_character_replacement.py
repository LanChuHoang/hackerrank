# https://leetcode.com/problems/longest-repeating-character-replacement/


class Solution:
    def characterReplacement_v1(self, s: str, k: int) -> int:
        frequency = [0 for _ in range(26)]
        n = len(s)
        res = 1
        for i in range(n):
            frequency = [0 for _ in range(26)]
            frequency[ord(s[i]) - ord("A")] += 1
            max_frequency = frequency[ord(s[i]) - ord("A")]
            for j in range(i + 1, n):
                frequency[ord(s[j]) - ord("A")] += 1
                max_frequency = max(max_frequency, frequency[ord(s[j]) - ord("A")])
                window_size = j - i + 1
                if max_frequency + k == window_size:
                    res = max(res, max_frequency + k)
            frequency[ord(s[i]) - ord("A")] -= 1
        return res

    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        n = len(s)
        res = 1

        l, r = 0, 0
        count[s[r]] = 1
        while l < n and r < n:
            w_len = r - l + 1
            max_count = max(count.values())
            num_changes = w_len - max_count

            if num_changes <= k:
                res = max(res, w_len)
                r += 1
                if r < n:
                    count[s[r]] = count.get(s[r], 0) + 1
            else:
                count[s[l]] -= 1
                l += 1
        return res


# s = Solution()
# print(s.characterReplacement("ABAB", k=2))
# print(s.characterReplacement(s="AABABBA", k=1))
# print(s.characterReplacement("XYZT", 4))
