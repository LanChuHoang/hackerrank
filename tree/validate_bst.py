# https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional
from utils import TreeNode, build_tree


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        cur_value = None
        result = True

        def dfs(node: Optional[TreeNode]):
            nonlocal result, cur_value
            if not node:
                return

            dfs(node.left)
            if cur_value is not None and cur_value >= node.val:
                result = False
            cur_value = node.val
            dfs(node.right)

        dfs(root)
        return result


print(Solution().isValidBST(build_tree([2, 1, 3])))
