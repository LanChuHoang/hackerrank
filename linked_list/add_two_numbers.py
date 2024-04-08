# https://leetcode.com/problems/add-two-numbers/

from typing import Optional
from utils import ListNode


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        carry = 0

        result_head = None
        prev_result_node = None
        while p1 is not None and p2 is not None:
            cur_sum = p1.val + p2.val + carry
            if cur_sum >= 10:
                cur_sum = cur_sum - 10
                carry = 1
            else:
                carry = 0
            new_result_node = ListNode(val=cur_sum)

            # First time
            if prev_result_node is None:
                result_head = new_result_node
                prev_result_node = new_result_node
            else:
                prev_result_node.next = new_result_node
                prev_result_node = new_result_node

            p1 = p1.next
            p2 = p2.next

        while p1 is not None:
            cur_sum = p1.val + 0 + carry
            if cur_sum >= 10:
                cur_sum = cur_sum - 10
                carry = 1
            else:
                carry = 0
            new_result_node = ListNode(val=cur_sum)
            prev_result_node.next = new_result_node
            prev_result_node = new_result_node
            p1 = p1.next

        while p2 is not None:
            cur_sum = 0 + p2.val + carry
            if cur_sum >= 10:
                cur_sum = cur_sum - 10
                carry = 1
            else:
                carry = 0
            new_result_node = ListNode(val=cur_sum)
            prev_result_node.next = new_result_node
            prev_result_node = new_result_node
            p2 = p2.next

        if carry == 1:
            prev_result_node.next = ListNode(val=1)

        return result_head
