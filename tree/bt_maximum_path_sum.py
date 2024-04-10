# https://leetcode.com/problems/binary-tree-maximum-path-sum/

from typing import Optional
from utils import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = root.val  # min root.val

        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0

            max_single_left = dfs(node.left)
            max_single_right = dfs(node.right)

            cur_len = max(max(max_single_left, max_single_right) + node.val, node.val)

            nonlocal global_max
            global_max = max(
                global_max,
                max_single_left + max_single_right + node.val,
                cur_len,
            )
            if node.left:
                global_max = max(global_max, max_single_left)
            if node.right:
                global_max = max(global_max, max_single_right)

            return cur_len

        dfs(root)
        return global_max
