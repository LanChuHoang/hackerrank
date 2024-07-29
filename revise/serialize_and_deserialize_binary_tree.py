# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

from collections import deque

# Idea: using bfs to serialize


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        node_strs = []
        queue = deque()
        queue.append(root)
        while queue:
            top = queue.popleft()
            if top is None:
                node_strs.append("N")
                continue
            node_strs.append(str(top.val))
            queue.append(top.left)
            queue.append(top.right)

        return ",".join(node_strs)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        node_strs = data.split(",")
        root = TreeNode(int(node_strs[0]))
        cur_level = [root]
        i = 1
        while cur_level:
            next_level = []
            for node in cur_level:
                left = node_strs[i]
                right = node_strs[i + 1]
                if left != "N":
                    node.left = TreeNode(int(left))
                    next_level.append(node.left)
                if right != "N":
                    node.right = TreeNode(int(right))
                    next_level.append(node.right)
                i += 2
            cur_level = next_level
        return root


def print_tree(root: TreeNode | None):
    if not root:
        return
    print(root.val, end=" ")
    if root.left:
        print(root.left.val, end=" ")
    if root.right:
        print(root.right.val, end=" ")
    print("\n")
    print_tree(root.left)
    print_tree(root.right)


# Your Codec object will be instantiated and called as such:
root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
right.left = TreeNode(4)
root.left = left
root.right = right
c = Codec()
s = c.serialize(root)
print(s)
print_tree(c.deserialize(s))
