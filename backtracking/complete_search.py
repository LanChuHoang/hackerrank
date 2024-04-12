def gen_subsets(n: int):
    subsets = []

    cur_subset = []

    def search(k: int):
        nonlocal cur_subset, subsets
        if k == n:
            subsets.append(cur_subset.copy())
            return

        # for each loop -> go left for gen the subset without k, go right for the subset with k
        # go left for gen the subset without k
        search(k + 1)

        # go right for the subset with k
        cur_subset.append(k)
        search(k + 1)

        # clean up
        cur_subset.pop()

    search(0)
    return subsets


print(gen_subsets(n=3))
