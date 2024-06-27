# https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def hIndex_v1(self, citations: list[int]) -> int:
        # Sort the citation array and then for each i, the number of papers that >= than citations[i]
        # is len(citations) - i
        # if the citations[i] >= num_papers then all of the papers from i to the end is >= its length
        # so the problem is find the minimumn i that satisfy this conditions

        citations.sort()
        length = len(citations)
        for i in range(length):
            num_papers = length - i
            if citations[i] >= num_papers:
                return num_papers

        return 0

    def hIndex(self, citations: list[int]) -> int:
        # Op 1: We can use b-search to find the minimum i that satisfy the conditions
        # citations[i] >= len(citations) - i
        # if citations[i] >= len(citations) - i then we decrease i to find the minimum one
        # else we increase the i to increase the citations[i] and decrease the num_papers
        # to match the condition

        citations.sort()
        n = len(citations)
        l, r = 0, n - 1

        result = 0
        while l <= r:
            m = (l + r) // 2
            num_papers = n - m
            if citations[m] >= num_papers:
                result = num_papers
                r = m - 1
            else:
                l = m + 1

        return result
