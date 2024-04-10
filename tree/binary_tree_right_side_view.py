# https://leetcode.com/problems/binary-tree-right-side-view/

from typing import Optional
from utils import TreeNode
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        queue = deque()
        queue.append(root)
        result = []

        while queue:
            num_nodes_at_cur_level = len(queue)
            most_right_node = None

            for _ in range(num_nodes_at_cur_level):
                node = queue.popleft()
                if node:
                    most_right_node = node.val
                    queue.append(node.left)
                    queue.append(node.right)

            if most_right_node is not None:
                result.append(most_right_node)

        return result
