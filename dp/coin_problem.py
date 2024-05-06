# competitive programming handbook

# find the smallest number of coins from a set of demoninations to form a specific amount
# top-down memorization
def recursive_count(amount: int, coin_set: list[int]):
    solved = dict()

    def solve(n: int):
        if n == 0:
            return 0

        if n in solved:
            return solved[n]

        min_count = n
        for c in coin_set:
            if n - c >= 0:
                min_count = min(min_count, solve(n - c) + 1)

        solved[n] = min_count

        return min_count

    return solve(amount)


# bottom-up table
def iterative_count(amount: int, coin_set: list[int]):
    dp_table = [amount] * (amount + 1)
    dp_table[0] = 0

    for n in range(1, len(dp_table)):
        for c in coin_set:
            if n - c >= 0:
                dp_table[n] = min(dp_table[n], dp_table[n - c] + 1)

    return dp_table[-1]


# find at least 1 optimal solution
def iterative_solve(amount: int, coin_set: list[int]):
    solved = [amount] * (amount + 1)
    solved[0] = 0
    chosen_coins = [float("inf")] * (amount + 1)

    for n in range(1, len(solved)):
        for c in coin_set:
            if n - c >= 0 and solved[n - c] + 1 < solved[n]:
                solved[n] = solved[n - c] + 1
                chosen_coins[n] = c

    solution = []
    i = amount
    while i > 0:
        chosen = chosen_coins[i]
        solution.append(chosen)
        i -= chosen

    return solution


# bottom-up count the number of solutions (not optimal included)
def interative_count_all(amount: int, coin_set: list[int]):
    count = [0] * (amount + 1)
    count[0] = 1
    for n in range(1, amount + 1):
        for c in coin_set:
            if n - c >= 0:
                count[n] += count[n - c]

    return count[-1]


def measure_perf():
    import timeit

    setup = "from __main__ import recursive_count, iterative_count"

    print("Performance of recursive_count")
    print(
        timeit.timeit(stmt="recursive_count(10, [1, 3, 4])", setup=setup, number=10000)
    )

    print("Performance of iterative_count")
    print(
        timeit.timeit(stmt="iterative_count(10, [1, 3, 4])", setup=setup, number=10000)
    )


if __name__ == "__main__":
    print(interative_count_all(amount=10, coin_set=[1, 3, 4]))
