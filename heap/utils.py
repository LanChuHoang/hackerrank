from PrettyPrint import PrettyPrintTree
from math import log

pt = PrettyPrintTree(
    lambda x: [x.left, x.right] if x else [], lambda x: x.val if x else None
)


class MaxHeap:
    def __init__(self) -> None:
        self.arr = []

    def insert(self, val):
        # Insert to the last position
        self.arr.append(val)

        # Heapify up until valid
        self._heapify_up(len(self.arr) - 1)

    def _heapify_up(self, idx: int):
        if idx <= 0 or self.arr[idx] <= self.arr[(idx - 1) // 2]:
            return
        # Swap with the parent node if the current node > the parent node
        parent_idx = (idx - 1) // 2
        self._swap(idx, parent_idx)
        self._heapify_up(parent_idx)

    def _swap(self, i: int, j: int):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp

    def top(self):
        return self.arr[0] if self.arr else None

    def remove_top(self):
        if not self.arr:
            return None
        if len(self.arr) == 1:
            top = self.arr.pop()
            return top

        # Swap the top with the last, then delete the last
        self._swap(0, len(self.arr) - 1)
        old_top = self.arr.pop()

        # Heapify down to correct the heap
        self._heapify_down(0)

        return old_top

    def _heapify_down(self, idx: int):
        if idx >= len(self.arr):
            return

        # find the largest element's index
        largest = idx
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        if (
            left_child_idx < len(self.arr)
            and self.arr[left_child_idx] > self.arr[largest]
        ):
            largest = left_child_idx
        if (
            right_child_idx < len(self.arr)
            and self.arr[right_child_idx] > self.arr[largest]
        ):
            largest = right_child_idx

        # if that index is not the current one, swap and continue from that
        if largest != idx:
            self._swap(idx, largest)
            self._heapify_down(largest)

    def build(self, val_list: list):
        for val in val_list:
            self.insert(val)

    def print(self):
        first = lambda h: 2**h - 1  # H stands for level height  # noqa: E731
        last = lambda h: first(h + 1)  # noqa: E731
        level = lambda heap, h: heap[first(h) : last(h)]  # noqa: E731
        prepare = lambda e, field: str(e).center(field)  # noqa: E731

        def hprint(heap, width=None):
            if width is None:
                width = max(len(str(e)) for e in heap)
            height = int(log(len(heap), 2)) + 1
            gap = " " * width
            for h in range(height):
                below = 2 ** (height - h - 1)
                field = (2 * below - 1) * width
                print(gap.join(prepare(e, field) for e in level(heap, h)))

        hprint(self.arr)
