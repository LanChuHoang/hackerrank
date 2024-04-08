# https://leetcode.com/problems/reverse-nodes-in-k-group/

from typing import Optional
from utils import ListNode, build_list


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        tail = head
        for _ in range(k):
            # If not enough group -> tail is None -> untouch
            if not tail:
                return head
            tail = tail.next

        next_head = tail
        new_head, new_tail = self.reverse(head, tail), head
        new_tail.next = self.reverseKGroup(next_head, k)
        return new_head

    def reverse(self, head: ListNode, tail: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur != tail:
            next_cur = cur.next
            cur.next = prev
            prev = cur
            cur = next_cur
        return prev


Solution().reverseKGroup(head=build_list([1, 2, 3, 4, 5]), k=5).print_list()
