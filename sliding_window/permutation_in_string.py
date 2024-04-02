# https://leetcode.com/problems/permutation-in-string/description/


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_frequency = dict()
        for c in s1:
            s1_frequency[c] = s1_frequency.get(c, 0) + 1

        start, end = 0, len(s1) - 1

        while end < len(s2):
            sub_s2_frequency = dict()
            for i in range(start, end + 1, 1):
                print(start, end, i)
                if s2[i] not in s1_frequency:
                    start = i + 1
                    end = start + len(s1) - 1
                    break
                else:
                    cur_freq = sub_s2_frequency.get(s2[i], 0)
                    max_freq = s1_frequency[s2[i]]
                    if cur_freq + 1 <= max_freq:
                        sub_s2_frequency[s2[i]] = cur_freq + 1
                        if i == end:
                            return True
                    else:
                        start += 1
                        end = start + len(s1) - 1

        return False


print(Solution().checkInclusion(s1="adc", s2="dcda"))
