from typing import Optional
from utils import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev_nth_node = None
        nth_node = head
        last_node = head
        # Setup the nth node and the last node distance
        for _ in range(n - 1):
            last_node = last_node.next

        while last_node.next is not None:
            prev_nth_node = nth_node
            nth_node = nth_node.next
            last_node = last_node.next

        if prev_nth_node is None:
            return nth_node.next

        next_nth_node = nth_node.next
        prev_nth_node.next = next_nth_node
        nth_node.next = None

        return head
