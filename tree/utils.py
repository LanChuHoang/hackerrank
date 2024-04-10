from PrettyPrint import PrettyPrintTree


pt = PrettyPrintTree(
    lambda x: [x.left, x.right] if x else [], lambda x: x.val if x else None
)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"({self.val})"

    def print_tree(self):
        pt(self)


def build_tree(val_list: list[int]) -> TreeNode:
    def build(idx: int) -> TreeNode | None:
        if idx >= len(val_list) or val_list[idx] is None:
            return None

        node = TreeNode(val=val_list[idx])
        node.left = build(idx=idx * 2 + 1)
        node.right = build(idx=idx * 2 + 2)
        return node

    return build(0)
