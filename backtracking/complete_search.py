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


def gen_permutation(n: int):
    result = []
    permutation = []
    chosen = [False] * n

    def dfs():
        nonlocal result, permutation
        if len(permutation) == n:
            result.append(permutation.copy())
            return

        for i in range(n):
            if chosen[i]:
                continue

            chosen[i] = True
            permutation.append(i)
            dfs()
            chosen[i] = False
            permutation.pop()

    dfs()
    return result


# print(gen_subsets(n=3))
print(gen_permutation(n=3))
