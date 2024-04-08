# https://leetcode.com/problems/linked-list-cycle/description/

from typing import Optional
from utils import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_node = set()

        cur_node = head
        while cur_node is not None:
            next_node = cur_node.next
            if next_node is not None and next_node in visited_node:
                return True
            visited_node.add(cur_node)
            cur_node = cur_node.next
        return False
