# https://leetcode.com/problems/copy-list-with-random-pointer/description/

from typing import Optional


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        old_to_new_map = {None: None}  # For the last None

        # Init copies
        cur_node = head
        while cur_node is not None:
            copy = Node(x=cur_node.val)
            old_to_new_map[cur_node] = copy
            cur_node = cur_node.next

        # Linking
        cur_node = head
        while cur_node is not None:
            copy = old_to_new_map.get(cur_node)
            copy.next = old_to_new_map.get(cur_node.next)
            copy.random = old_to_new_map.get(cur_node.random)
            cur_node = cur_node.next

        return old_to_new_map[head]
