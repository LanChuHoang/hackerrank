# https://leetcode.com/problems/balanced-binary-tree/description/

from typing import Optional
from utils import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance_and_height(node: Optional[TreeNode]):
            if not node:
                return True, -1

            (is_left_balance, left_h) = check_balance_and_height(node.left)
            (is_right_balance, right_h) = check_balance_and_height(node.right)
            is_balance = (
                is_left_balance and is_right_balance and abs(left_h - right_h) <= 1
            )
            return is_balance, max(left_h, right_h) + 1

        return check_balance_and_height(root)[0]
