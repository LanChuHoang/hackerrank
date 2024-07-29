# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import Optional
from utils import TreeNode


class Solution:
    def buildTree_v1(
        self, preorder: list[int], inorder: list[int]
    ) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root

    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        # Idea: for each preorder array
        # preorder[0] always is the root
        # the remain part is the combination of the left nodes and the right nodes
        # = left_node1, left_node2, ..., right_node1, right_node2, ...
        # -> We need to find the mid point between the left node part and the right
        # node part
        # -> We use the inorder array to find the number of left nodes and right nodes
        # because the inorder array always has the form like this
        # some_left_nodes, root, some_right_nodes
        # -> We find the root node's index -> then use it to calculate the number of left and
        # right nodes

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
