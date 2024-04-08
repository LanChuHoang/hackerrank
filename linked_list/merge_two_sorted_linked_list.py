# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
from utils import ListNode, build_list


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        p1 = list1
        p2 = list2

        result = []
        while p1 is not None and p2 is not None:
            cur_node = result[-1] if result else None
            if p1.val > p2.val:
                result.append(ListNode(val=p2.val, next=None))
                if cur_node:
                    cur_node.next = result[-1]
                p2 = p2.next
            else:
                result.append(ListNode(val=p1.val, next=None))
                if cur_node:
                    cur_node.next = result[-1]
                p1 = p1.next

        while p1 is not None:
            cur_node = result[-1] if result else None
            result.append(ListNode(val=p1.val, next=None))
            if cur_node is not None:
                cur_node.next = result[-1]
            p1 = p1.next

        while p2 is not None:
            cur_node = result[-1] if result else None
            result.append(ListNode(val=p2.val, next=None))
            if cur_node is not None:
                cur_node.next = result[-1]
            p2 = p2.next

        return result[0] if result else None


head1 = build_list([])
head2 = build_list([1])
head3 = Solution().mergeTwoLists(head1, head2)
head1.print_list()
head2.print_list()
head3.print_list()
