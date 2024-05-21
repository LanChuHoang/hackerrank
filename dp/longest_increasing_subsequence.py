# competitive programming handbook

# find the longest increasing sub sequence in a given array

# bottom-up: O(n^2)
# idea: len(k) is the max len that end at index k
# len(k) = len(i) + 1 where
# i < k and arr[i] < arr[k]
# len(i) is largest


def o_squared_lis(arr: list[int]):
    max_so_far = 1
    max_len = [1] * len(arr)
    for k in range(1, len(arr)):
        for i in range(0, k):
            if arr[i] < arr[k]:
                max_len[k] = max(max_len[k], max_len[i] + 1)
        max_so_far = max(max_so_far, max_len[k])
    return max_so_far


def o_nlogn_lis(arr: list[int]):
    # last_idxs: arr of size n to store the last idx of a set of lists that has length i + 1
    # -> each loop if we encounter the new element that larger that the last element of the largest list
    # -> extend the list
    # if not, change the last element of suitable list, to maximize the protential to form a largest list in the future
    # (because we replace the current element with the smallest larger one -> so the larger one is useless
    # -> if we keep the larger -> the future list is always worst)
    if not arr:
        return None

    last_idxs = [-1] * len(arr)
    prev_idxs = [-1] * len(arr)

    last_idxs[0] = 0
    max_length_so_far = 1
    for i in range(1, len(arr)):
        # check whether to extend the list or not

        # if yes -> store new list + idx of the prev el to trace back
        if arr[i] > arr[last_idxs[max_length_so_far - 1]]:
            last_idxs[max_length_so_far] = i
            prev_idxs[i] = last_idxs[max_length_so_far - 1]
            max_length_so_far += 1

        # else -> binary search the lis_last_idx_list to find the suitable element to replace
        else:
            l, r = 0, i - 1  # noqa: E741
            while l <= r:
                m = (l + r) // 2
                mid_el = arr[last_idxs[m]]
                if arr[i] == mid_el:
                    last_idxs[m] = i
                    break
                elif arr[i] < mid_el:
                    r = m - 1
                else:
                    l = m + 1  # noqa: E741
            last_idxs[r + 1] = i

    # trace back to compose the result
    i = last_idxs[max_length_so_far - 1]
    result = []
    while i != -1:
        result.append(arr[i])
        i = prev_idxs[i]
    result.reverse()
    return result


if __name__ == "__main__":
    print(o_nlogn_lis([6, 2, 5, 1, 7, 4, 8, 3]))
