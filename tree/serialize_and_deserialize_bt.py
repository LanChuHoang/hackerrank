# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

from utils import TreeNode, build_tree


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        val_str_list = []

        def dfs(node):
            nonlocal val_str_list
            if not node:
                val_str_list.append("N")
                return

            val_str_list.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(val_str_list)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        val_list = data.split(",")

        i = 0

        def dfs():
            nonlocal i
            if val_list[i] == "N":
                i += 1
                return None

            node = TreeNode(val=(int(val_list[i])))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


root = build_tree([1, 2, 3, None, None, 4, 5, None, None, None, None, 6, 7, None, None])
root.print_tree()
msg = Codec().serialize(root)
print(msg)
Codec().deserialize(msg).print_tree()
