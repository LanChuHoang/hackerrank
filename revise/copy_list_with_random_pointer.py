# https://leetcode.com/problems/copy-list-with-random-pointer/description/


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self) -> str:
        return f"(x: {self.val}, next: {self.next.val if self.next else None}, random: {self.random.val if self.random else None})"


class Solution:
    def copyRandomList_v1(self, head):
        # Idea: use 2 array and one dict to store the old nodes and the new nodes
        # then link the new node later

        if not head:
            return None

        nodes = []
        node_idx = dict()
        next_node = head
        while next_node:
            node_idx[next_node] = len(nodes)
            nodes.append(next_node)
            next_node = next_node.next

        new_nodes = [Node(n.val) for n in nodes]
        n = len(new_nodes)
        new_nodes.append(None)
        for i in range(n):
            new_nodes[i].next = new_nodes[i + 1]
            new_nodes[i].random = (
                new_nodes[node_idx[nodes[i].random]] if nodes[i].random else None
            )
        return new_nodes[0]

    def copyRandomList_v2(self, head):
        if not head:
            return None

        # Init phase -> copy all old nodes to new nodes without links
        old_to_new = {None: None}
        cur_node = head
        while cur_node:
            new_node = Node(cur_node.val)
            old_to_new[cur_node] = new_node
            cur_node = cur_node.next

        # Linking phase -> link all new nodes to each other
        cur_node = head
        while cur_node:
            new_node = old_to_new[cur_node]
            new_node.next = old_to_new[cur_node.next]
            new_node.random = old_to_new[cur_node.random]
            cur_node = cur_node.next

        return old_to_new[head]

    def copyRandomList(self, head):
        if not head:
            return None

        # Init and mapping phase: insert the new node between 2 old nodes
        # and link them to create the map
        cur_node = head
        while cur_node:
            cur_node.next = Node(cur_node.val, cur_node.next)
            cur_node = cur_node.next.next

        # Link random pointers of the new nodes
        cur_node = head
        while cur_node:
            if cur_node.random:
                copy = cur_node.next
                copy.random = cur_node.random.next
            cur_node = cur_node.next.next

        # Link the next pointers of the new nodes
        # and restore the original list
        cur_node = head
        new_head = cur_node.next
        while cur_node:
            copy = cur_node.next
            cur_node.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            cur_node = cur_node.next

        return new_head


def create_list(arr: list[list[int | None]]):
    n = len(arr)
    res = []
    for i in range(n):
        res.append(Node(arr[i][0]))
    res.append(None)
    for i in range(n):
        res[i].next = res[i + 1]
        res[i].random = arr[i][1] if arr[i][1] is None else res[arr[i][1]]
    return res[0]


def print_list(head: Node):
    next_node = head
    while next_node:
        print(next_node)
        next_node = next_node.next


s = Solution()
h = create_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
print_list(h)
print_list(s.copyRandomList(h))
