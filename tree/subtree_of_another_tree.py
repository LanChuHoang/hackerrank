# https://leetcode.com/problems/subtree-of-another-tree/description/

from typing import Optional
from utils import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        is_same = (p is None and q is None) or (
            p is not None and q is not None and p.val == q.val
        )
        if not is_same:
            return False
        if p is None and p is None:
            return True
        is_left_same = self.isSameTree(p.left, q.left)
        if not is_left_same:
            return False
        is_right_same = self.isSameTree(p.right, q.right)
        return is_right_same

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
