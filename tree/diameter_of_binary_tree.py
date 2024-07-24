# https://leetcode.com/problems/diameter-of-binary-tree/description/

from typing import Optional
from utils import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Idea: diameter d of a root is
        # max(d_left, d_right, max_left_h + max_left_right + 2)

        def diameter_height(node: Optional[TreeNode]):
            if not node:
                return 0, -1

            (left_d, left_h) = diameter_height(node.left)
            (right_d, right_h) = diameter_height(node.right)
            return max(left_d, right_d, left_h + right_h + 2), max(left_h, right_h) + 1

        return diameter_height(root)[0]
