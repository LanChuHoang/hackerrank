def find_possible_combinations(weights: list[int]):
    """
    Problem: find all possible combinations from a list of weights.
    Each weight is only be used once
    Solution:
    x: is the target sum to check possibility
    k: is the first number of weights to use
    w_k: is the last weight from first k weights
    - possible(x, k) = possible(x - w_k, k - 1) or possible(x, k - 1)
    possible(x-w_k, k-1): use the w_k in the combination
    possible(x, k-1): not use the w_k in the combination
    --> The general idea is for a given x, and k number of weights
    x is possible to form if we can form x-w_k with k-1 weights or x with k - 1 weights
    --> build the table to store the calculation
    go from possible(0, 0) to possible(max_sum, k)
    """
    max_sum = sum(weights)
    possible = [
        [False for _ in range(0, max_sum + 1)] for _ in range(0, len(weights) + 1)
    ]
    possible[0][0] = True
    for k in range(1, len(possible)):
        for x in range(len(possible[0])):
            cur_w = weights[k - 1]
            use_cur_w = possible[k - 1][x - cur_w]
            not_use_cur_w = possible[k - 1][x]
            possible[k][x] = use_cur_w or not_use_cur_w
    return possible


def pretty_print_matrix(matrix: list[list[int]]):
    s = [["X" if e else "" for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = "\t".join("{{:{}}}".format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print("\n".join(table))


if __name__ == "__main__":
    weights = [1, 3, 3, 5]
    pretty_print_matrix(find_possible_combinations(weights))
