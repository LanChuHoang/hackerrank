# https://leetcode.com/problems/snapshot-array/description/?envType=study-plan-v2&envId=binary-search


class SnapshotArray:
    def __init__(self, length: int):
        self.hist = [[[0, 0]] for _ in range(length)]
        self.num_snaps = 0

    def set(self, index: int, val: int) -> None:
        if self.hist[index][-1][0] == self.num_snaps:
            self.hist[index][-1][1] = val
        else:
            self.hist[index].append([self.num_snaps, val])

    def snap(self) -> int:
        snap_id = self.num_snaps
        self.num_snaps += 1
        return snap_id

    def get(self, index: int, snap_id: int) -> int:
        hist_list = self.hist[index]

        l, r = 0, len(hist_list) - 1
        result = hist_list[-1][1]
        while l <= r:
            m = (l + r) // 2
            if hist_list[m][0] == snap_id:
                result = hist_list[m][1]
                break
            elif hist_list[m][0] < snap_id:
                result = hist_list[m][1]
                l = m + 1
            else:
                r = m - 1
        return result


# obj = SnapshotArray(3)
# obj.set(1, 6)
# print(obj.snap())
# print(obj.snap())
# obj.set(1, 19)
# obj.set(0, 4)
# print(obj.get(2, 1))
# print(obj.get(2, 0))
# print(obj.get(0, 1))
