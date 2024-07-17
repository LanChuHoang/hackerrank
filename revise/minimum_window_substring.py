class Solution:
    def check_valid(self, s_count: dict, t_count: dict):
        for k, v in t_count.items():
            s_v = s_count.get(k, 0)
            if s_v < v:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        s_count = dict()
        t_count = dict()
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1

        l, r, n = 0, 0, len(s)
        res, res_l, res_r = n + 1, 0, 0
        if s[r] in t_count:
            s_count[s[r]] = 1

        while l < n and r < n:
            is_valid = self.check_valid(s_count, t_count)

            if is_valid:
                wlen = r - l + 1
                if wlen < res:
                    res, res_l, res_r = wlen, l, r

                if s[l] in t_count:
                    s_count[s[l]] -= 1
                l += 1
            else:
                r += 1
                if r < n and s[r] in t_count:
                    s_count[s[r]] = s_count.get(s[r], 0) + 1
        return s[res_l : res_r + 1] if res <= n else ""


# s = Solution()
# print(s.minWindow(s="ADOBECODEBANC", t="ABC"))
# print(s.minWindow(s="a", t="a"))
# print(s.minWindow(s="a", t="aa"))
