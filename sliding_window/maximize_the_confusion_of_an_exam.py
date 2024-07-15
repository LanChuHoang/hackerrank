# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l, r = 0, 0
        t_count, f_count = 0, 0
        if answerKey[0] == "T":
            t_count = 1
        else:
            f_count = 1
        n = len(answerKey)
        res = 1
        while l < n and r < n:
            w_len = r - l + 1
            max_count = max(t_count, f_count)
            num_changes = w_len - max_count

            if num_changes <= k:
                res = max(res, w_len)
                r += 1
                if r < n:
                    if answerKey[r] == "T":
                        t_count += 1
                    else:
                        f_count += 1
            else:
                if answerKey[l] == "T":
                    t_count -= 1
                else:
                    f_count -= 1
                l += 1
        return res


s = Solution()

print(s.maxConsecutiveAnswers(answerKey="TTFF", k=2))
print(s.maxConsecutiveAnswers(answerKey="TFFT", k=1))
print(s.maxConsecutiveAnswers(answerKey="TTFTTFTT", k=1))
