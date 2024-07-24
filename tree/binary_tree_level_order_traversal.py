# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import Optional, List
from utils import TreeNode, build_tree
from collections import deque


class Solution:
    def levelOrder_v1(self, root: Optional[TreeNode]) -> list[list[int]]:
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


result = Solution().levelOrder(build_tree([1, 2, None, 3, None, 4, None, 5]))
print(result)
