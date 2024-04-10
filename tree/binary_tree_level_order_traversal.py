# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import Optional
from utils import TreeNode, build_tree
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        queue = deque()
        result = []
        queue.append(root)

        while queue:
            num_nodes_at_cur_level = len(queue)
            level = []
            for _ in range(num_nodes_at_cur_level):
                node = queue.popleft()
                if node and node.val is not None:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                result.append(level)

        return result


result = Solution().levelOrder(build_tree([1, 2, None, 3, None, 4, None, 5]))
print(result)
