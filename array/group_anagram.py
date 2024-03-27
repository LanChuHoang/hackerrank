# https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group = dict()
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in group:
                group[sorted_s] = [s]
            else:
                group[sorted_s].append(s)
        return list(group.values())
