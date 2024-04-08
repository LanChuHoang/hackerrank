# https://leetcode.com/problems/reorder-list/description/

from typing import Optional
from utils import ListNode, build_list


class Solution:
    def count_list(self, head: Optional[ListNode]):
        count = 0
        cur_node = head
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next

        return count

    def find_mid_node(self, head: Optional[ListNode]):
        length = self.count_list(head)
        mid = length // 2
        mid_node = head
        for _ in range(1, mid + 1, 1):
            mid_node = mid_node.next
        return mid_node

    def split_in_half(
        self, head: Optional[ListNode]
    ) -> tuple[Optional[ListNode], Optional[ListNode]]:
        length = self.count_list(head)
        if length <= 2:
            return head, None

        mid = length // 2
        mid_node = head
        for _ in range(1, mid + 1, 1):
            mid_node = mid_node.next

        head2 = mid_node.next
        mid_node.next = None
        return head, head2

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        cur_node = head
        while cur_node is not None:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        return prev_node

    def merge(
        self, head1: Optional[ListNode], head2: Optional[ListNode]
    ) -> Optional[ListNode]:
        cur_node1 = head1
        cur_node2 = head2

        while cur_node1 is not None and cur_node2 is not None:
            next_node1 = cur_node1.next
            next_node2 = cur_node2.next
            cur_node1.next = cur_node2
            cur_node2.next = next_node1
            cur_node1 = next_node1
            cur_node2 = next_node2

        return head1

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        head1, head2 = self.split_in_half(head)
        if head2 is None:
            return head1
        head2 = self.reverse(head2)
        return self.merge(head, head2)


Solution().reorderList(head=build_list([1, 2, 3, 4, 5])).print_list()
