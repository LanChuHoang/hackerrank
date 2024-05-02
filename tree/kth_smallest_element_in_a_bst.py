# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

from typing import Optional
from utils import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = None
        visited_nodes = []

        def dfs(node: Optional[TreeNode]):
            if not node:
                return

            nonlocal result, visited_nodes
            dfs(node.left)
            visited_nodes.append(node.val)
            if len(visited_nodes) == k:
                result = visited_nodes[-1]
            dfs(node.right)

        dfs(root)
        return result
