# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional
from utils import ListNode, build_list


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        cur_node = head
        while cur_node is not None:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        return prev_node


arr = [1, 2, 3, 4, 5]
head = build_list(arr)
head.print_list()
head = Solution().reverseList(head)
head.print_list()
