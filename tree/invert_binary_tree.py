# https://leetcode.com/problems/invert-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
from utils import TreeNode, build_tree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        left = root.left
        root.left = root.right
        root.right = left

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        return root


root = build_tree([4, 2, 7, 1, 3, 6, 9])
root.print_tree()
inverted = Solution().invertTree(root)
inverted.print_tree()
