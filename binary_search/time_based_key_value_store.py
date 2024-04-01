# https://leetcode.com/problems/time-based-key-value-store/description/


class TimeMap:

    def __init__(self):
        self.state = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.state:
            self.state[key] = [(timestamp, value)]
        else:
            self.state[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        keyed_state = self.state.get(key, [])
        return self.get_max_prev_timestamp(keyed_state, timestamp)

    def get_max_prev_timestamp(
        self, keyed_state: list[tuple[int, str]], timestamp: int
    ) -> tuple[int, str]:
        i, j = 0, len(keyed_state) - 1
        res = None
        while i <= j:
            k = (i + j) // 2
            if keyed_state[k][0] == timestamp:
                res = keyed_state[k]
                break
            elif keyed_state[k][0] < timestamp:
                if not res or keyed_state[k][0] > res[0]:
                    res = keyed_state[k]
                i = k + 1
            else:
                j = k - 1
        return res[1] if res else ""


# # Your TimeMap object will be instantiated and called as such:
# timeMap = TimeMap()
# timeMap.set(
#     "foo", "bar", 10
# )  # store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.set(
#     "foo", "bar2", 20
# )  # store the key "foo" and value "bar2" along with timestamp = 4.
# print(timeMap.get("foo", 5))
# print(timeMap.get("foo", 10))
# print(timeMap.get("foo", 15))
# print(timeMap.get("foo", 20))
# print(timeMap.get("foo", 25))
