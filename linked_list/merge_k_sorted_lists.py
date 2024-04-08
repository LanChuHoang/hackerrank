# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List, Optional
from utils import ListNode

import heapq


class Solution:
    def mergeKLists_brute_force(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        head = None
        cur_node = None
        while True:
            min_node_index = None
            for i in range(len(lists)):
                if lists[i] is None:
                    continue

                if min_node_index is None or lists[i].val < lists[min_node_index].val:
                    min_node_index = i

            min_node = lists[min_node_index] if min_node_index is not None else None

            if cur_node is not None:
                cur_node.next = min_node
            cur_node = min_node

            if head is None:
                head = cur_node

            if min_node is None:
                break
            lists[min_node_index] = lists[min_node_index].next

        return head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i))
                lists[i] = node.next

        dummy = ListNode()
        cur_node = dummy
        while heap:
            # Get the min element
            val, idx = heapq.heappop(heap)
            # Create new node and insert to the list
            new_node = ListNode(val)
            cur_node.next = new_node
            cur_node = cur_node.next
            # Move the pointer to the next element and add the next element to the heap
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next

        return dummy.next
