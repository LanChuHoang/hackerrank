from collections import defaultdict


class Solution:
    def winningPlayerCount(self, n: int, pick: list[list[int]]) -> int:
        wins = [False for _ in range(n)]
        picked_balls = [defaultdict(int) for _ in range(n)]
        res = 0
        for player, ball in pick:
            picked_balls[player][ball] += 1
            if not wins[player] and picked_balls[player][ball] > player:
                wins[player] = True
                res += 1
        return res
