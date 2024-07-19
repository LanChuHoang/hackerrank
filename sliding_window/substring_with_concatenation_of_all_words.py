# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/?envType=study-plan-v2&envId=top-interview-150

from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        s_len, w_len, num_w = len(s), len(words[0]), len(words)
        w_count = Counter(words)
        res = []
        for i in range(w_len):
            left, right = i, i
            s_count = defaultdict(int)
            have = 0

            while right + w_len <= s_len:
                word = s[right : right + w_len]
                right += w_len

                if word in w_count:
                    s_count[word] += 1
                    have += 1

                    while s_count[word] > w_count[word]:
                        left_word = s[left : left + w_len]
                        s_count[left_word] -= 1
                        have -= 1
                        left += w_len

                    if have == num_w:
                        res.append(left)
                else:
                    s_count.clear()
                    have = 0
                    left = right
        return res
