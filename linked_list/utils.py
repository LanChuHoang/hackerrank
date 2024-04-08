from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"Node({self.val})"

    def print_list(self):
        output = []
        cur_node = self
        while cur_node is not None:
            output.append(str(cur_node))
            cur_node = cur_node.next

        print("->".join(output))


def build_list(arr: list) -> Optional[ListNode]:
    def build_node(i: int):
        if i >= len(arr):
            return None

        next_node = build_node(i + 1)
        return ListNode(val=arr[i], next=next_node)

    head = build_node(0)
    return head
