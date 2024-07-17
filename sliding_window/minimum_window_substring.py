class Solution:
    def minWindow_v1(self, s: str, t: str) -> str:
        # Idea: maintain a sliding window in s
        # try to extend the right boundary until the current window is a valid solution
        # then reduce the left boundary until it breaks the valid condition
        # during the reduce phase -> record the shortest window
        # Idea: How to check the valid condition
        # Simply storing 2 dicts, and maintain 2 variables have and need
        # every time we meet some char that break the valid condition -> update have
        s_count = dict()
        t_count = dict()
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1

        l, r, n = 0, 0, len(s)
        res, res_l, res_r = n + 1, 0, 0
        have, need = 0, len(t_count)
        if s[r] in t_count:
            s_count[s[r]] = 1
            if s_count[s[r]] == t_count[s[r]]:
                have = 1

        while l < n and r < n:
            if have == need:
                wlen = r - l + 1
                if wlen < res:
                    res, res_l, res_r = wlen, l, r

                if s[l] in t_count:
                    s_count[s[l]] -= 1
                    if s_count[s[l]] == t_count[s[l]] - 1:
                        have -= 1
                l += 1
            else:
                r += 1
                if r < n and s[r] in t_count:
                    s_count[s[r]] = s_count.get(s[r], 0) + 1
                    if s_count[s[r]] == t_count[s[r]]:
                        have += 1
        return s[res_l : res_r + 1] if res <= n else ""

    def minWindow(self, s: str, t: str):
        # Idea: optimize validation check by using a single map as a array
        # and a single variable need
        # In the expand phase:
        # - if the count of the current char c > 0
        # (means c in t and the current window doesnt have enough number of c)
        # -> decrease need
        # - Then decrease the count of the current char (dont care whether c in t or not,
        # because if c in t -> the count will be 0, ow negative -> so in the reduce phase
        # we can use it as a flag of what in t or not, for update the "need")
        # In the reduce phase:
        # - while need == 0:
        #   - update the solution
        #   - if we meet some count that == 0, that mean if we shrink the left, the number of that char
        # in the window < the required from t
        # -> so we need to increase the "need"
        #   - char that not in t does not effect, because count never > 0 (at most 0) so it never meets the
        # above check
        if not s or not t or len(s) < len(t):
            return ""

        visit_times = [0] * (ord("z") + 1)
        for c in t:
            visit_times[ord(c)] += 1

        l, r, n = 0, 0, len(s)
        res, res_l = n + 1, 0
        need = len(t)
        while r < n:
            if visit_times[ord(s[r])] > 0:
                need -= 1
            visit_times[ord(s[r])] -= 1
            r += 1

            while need == 0:
                wlen = r - l
                if wlen < res:
                    res, res_l = wlen, l

                if visit_times[ord(s[l])] == 0:
                    need += 1
                visit_times[ord(s[l])] += 1
                l += 1
        return s[res_l : res_l + res] if res <= n else ""


# s = Solution()
# print(s.minWindow(s="ADOBECODEBANC", t="ABC"))
# print(s.minWindow(s="a", t="a"))
# print(s.minWindow(s="a", t="aa"))
