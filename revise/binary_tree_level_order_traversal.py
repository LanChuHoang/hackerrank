# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append(root)

        res = []
        while queue:
            level_len = len(queue)
            res.append([])
            for _ in range(level_len):
                node = queue.popleft()
                if node is not None:
                    res[-1].append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

        return res


print(Solution().levelOrder(None))
