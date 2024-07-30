# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/?envType=daily-question&envId=2024-07-30


class Solution:
    def minimumDeletions_v1(self, s: str) -> int:
        # Idea: find the sweet point where the total number of invalid
        # charaters is mimimumn
        # The number of invalid charaters = the number of bs in the left part
        # + the number of as in the right part

        num_right_a = 0
        for c in s:
            if c == "a":
                num_right_a += 1
        num_left_b = 0

        n = len(s)
        res = n
        for i in range(n):
            num_remove = num_left_b + num_right_a
            res = min(res, num_remove)
            if s[i] == "a":
                num_right_a -= 1
            else:
                num_left_b += 1
        res = min(res, num_left_b + num_right_a)
        return res

    def minimumDeletions(self, s):
        # Idea:
        # The minimum of characters to remove is the number of a that after b
        # for example:
        # bbaaaaabb -> 2 As after 2 Bs -> only need to remove 2 Bs
        # aabaabbbaab -> 1 A after 1 B, 2 As after 2 Bs -> remove the first b and then 2 As after

        res, b_count = 0, 0
        for c in s:
            if c == "b":
                b_count += 1
            elif b_count > 0:
                res += 1
                b_count -= 1
        return res


s = Solution()
print(s.minimumDeletions("aababbab"))
print(s.minimumDeletions("bbaaaaabb"))
