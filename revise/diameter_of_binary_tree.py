# https://leetcode.com/problems/diameter-of-binary-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Idea: diameter d of a root is
        # max(d_left, d_right, max_left_h + max_left_right + 2)

        res = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal res

            if not node:
                return -1

            max_left_length = dfs(node.left)
            max_right_length = dfs(node.right)
            res = max(res, max_left_length + max_right_length + 2)
            return max(max_left_length, max_right_length) + 1

        dfs(root)
        return res


# nodes = [TreeNode(x) for x in [1, 2, 3, 4, 5]]
# nodes[0].left = nodes[1]
# nodes[0].right = nodes[2]
# nodes[1].left = nodes[3]
# nodes[1].right = nodes[4]
# s = Solution()
# print(s.diameterOfBinaryTree(nodes[0]))
# n1 = TreeNode(1, left=TreeNode(2))
# print(s.diameterOfBinaryTree(n1))
