# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

from utils import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def check_good_node(node: TreeNode, prev_max: int):
            nonlocal result
            if not node:
                return

            cur_max = prev_max
            if node.val >= prev_max:
                result += 1
                cur_max = node.val

            check_good_node(node.left, prev_max=cur_max)
            check_good_node(node.right, prev_max=cur_max)

        check_good_node(root, root.val)
        return result
