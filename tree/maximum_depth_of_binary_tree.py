# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from typing import Optional
from utils import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
