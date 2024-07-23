# Definition for singly-linked list.
from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        heap = []
        for i, head in enumerate(lists):
            if head is not None:
                heapq.heappush(heap, (head.val, i))

        dummy = ListNode()
        cur_node = dummy
        while heap:
            _, i = heapq.heappop(heap)
            min_node = lists[i]
            lists[i] = min_node.next

            if min_node.next:
                heapq.heappush(heap, (min_node.next.val, i))

            cur_node.next = min_node
            cur_node = cur_node.next
        return dummy.next
