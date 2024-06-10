# https://leetcode.com/problems/word-break/description/


class Solution:
    def wordBreak_v1(self, s: str, wordDict: list[str]) -> bool:
        word_dict = set(wordDict)

        def solvable(i: int, cur_sub_s: str):
            if i >= len(s):
                return cur_sub_s in word_dict

            # split at this i and check the rest
            # not split at this i and check the rest
            cur_sub_s = cur_sub_s + s[i]
            return (cur_sub_s in word_dict and solvable(i + 1, "")) or solvable(
                i + 1, cur_sub_s
            )

        return solvable(0, "")

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[-1] = True

        for i in reversed(range(len(s))):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]

                if dp[i]:
                    break
        return dp[0]


# solution = Solution()
# print(solution.wordBreak("leetcodefun", ["leet", "code", "fun", "leetcode"]))
# print(solution.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
# print(solution.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
