# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree_v1(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None

        root = TreeNode(preorder[0])
        root_indorder_idx = inorder.index(preorder[0])
        root.left = self.buildTree(
            preorder[1 : root_indorder_idx + 1], inorder[:root_indorder_idx]
        )
        root.right = self.buildTree(
            preorder[root_indorder_idx + 1 :], inorder[root_indorder_idx + 1 :]
        )
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {v: i for i, v in enumerate(inorder)}

        def build(pre_start: int, pre_end: int, in_start: int, in_end: int):
            root = TreeNode(preorder[pre_start])
            root_inorder_idx = inorder_idx[root.val]
            num_left = root_inorder_idx - in_start
            num_right = in_end - root_inorder_idx
            if num_left:
                root.left = build(
                    pre_start + 1, pre_start + num_left, in_start, root_inorder_idx - 1
                )
            if num_right:
                root.right = build(
                    pre_start + num_left + 1, pre_end, root_inorder_idx + 1, in_end
                )
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)


# s = Solution()
# print(s.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]))
# print(s.buildTree(preorder=[-1], inorder=[-1]))
