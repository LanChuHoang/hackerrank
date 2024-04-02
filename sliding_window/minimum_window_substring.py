# https://leetcode.com/problems/minimum-window-substring/description/


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count_t, count_window = dict(), dict()

        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        have, need = len(count_window), len(count_t)
        start = 0
        min_length, res_start, res_end = None, None, None

        for end in range(len(s)):
            if s[end] not in count_t:
                continue

            count_window[s[end]] = count_window.get(s[end], 0) + 1
            have = len(count_window)

            if count_window[s[end]] >= count_t[s[end]]:
                print(start, end, count_window, count_t)

                # Try to minimize the solution
                while have == need:
                    print("found", start, end, count_window, count_t)
                    cur_length = end - start + 1
                    if min_length is None or cur_length < min_length:
                        min_length = cur_length
                        res_start = start
                        res_end = end

                    # Pop the first element
                    if s[start] in count_t:
                        count_window[s[start]] -= 1
                        count_start = count_window[s[start]]
                        if count_start == 0:
                            del count_window[s[start]]
                            have = len(count_window)
                        if count_start < count_t[s[start]]:
                            start += 1
                            break
                    start += 1

        return s[res_start : res_end + 1] if res_start is not None else ""


# print(Solution().minWindow(s="cabwefgewcwaefgcf", t="cae"))
print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))
