# https://leetcode.com/problems/lru-cache/description/


class ListNode:
    def __init__(self, key=0, val=0, next_node=None, prev_node=None) -> None:
        self.key = key
        self.val = val
        self.next = next_node
        self.prev = prev_node

    def __str__(self) -> str:
        return f"Node({self.key}, {self.val})"


class LRUCache:
    def __init__(self, capacity: int, debug=False):
        self.capacity = capacity
        self.debug = debug
        self.node_dict: dict[int, ListNode] = dict()
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.node_dict:
            node = self.node_dict[key]
            value = node.val
            self._move_to_recent(node)
        else:
            value = -1
        self._print(f"GET ({key}) -> value {value}")
        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.node_dict:
            new_node = ListNode(key, value)
            self._append_node(new_node)
            self.node_dict[key] = new_node
            self._reduce_cache_if_full()
        else:
            to_update_node = self.node_dict[key]
            to_update_node.val = value
            self._move_to_recent(to_update_node)

        self._print(f"PUT ({key}, {value})")

    def _move_to_recent(self, node: ListNode):
        if node.key == self.tail.key:
            return
        self._delete_node(node)
        self._append_node(node)

    def _reduce_cache_if_full(self):
        if len(self.node_dict) > self.capacity:
            least_use_node = self.head
            self._delete_node(least_use_node)
            del self.node_dict[least_use_node.key]

    def _append_node(self, node: ListNode):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def _delete_node(self, node: ListNode):
        prev_node = node.prev
        next_node = node.next
        if prev_node is not None:
            prev_node.next = next_node
        if next_node is not None:
            next_node.prev = prev_node
        node.prev = None
        node.next = None
        if node.key == self.head.key:
            self.head = next_node
        if node.key == self.tail.key:
            self.tail = prev_node

    def _print(self, op: str):
        if not self.debug:
            return

        def print_list():
            nodes = []
            cur_node = self.head
            while cur_node is not None:
                nodes.append(str(cur_node))
                cur_node = cur_node.next
            return "->".join(nodes) + f", HEAD {self.head}, TAIL {self.tail}"

        def print_dict():
            items = [f"{key}: {str(value)}" for key, value in self.node_dict.items()]
            return "{" + ",".join(items) + "}"

        print(
            op,
            "\tNODE_DICT",
            print_dict(),
            "\tLIST",
            print_list(),
        )


lRUCache = LRUCache(3, debug=True)
lRUCache.put(1, 1)  # cache is {1=1}
lRUCache.put(2, 2)  # cache is {1=1, 2=2}
lRUCache.put(3, 3)  # cache is {1=1}
lRUCache.put(4, 4)  # cache is {1=1, 2=2}
lRUCache.get(4)  # return 1
lRUCache.get(3)  # return 1
lRUCache.get(2)  # return 1
lRUCache.get(1)  # return 1
lRUCache.put(5, 5)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(1)  # returns -1 (not found)
lRUCache.get(2)  # returns -1 (not found)
lRUCache.get(3)  # returns -1 (not found)
lRUCache.get(4)  # returns -1 (not found)
lRUCache.get(5)  # returns -1 (not found)
