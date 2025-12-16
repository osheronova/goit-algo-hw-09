"""
Cash register system for optimal change delivery.
Greedy algorithm and Dynamic Programming (minimum coins).
"""

from __future__ import annotations

import time
from typing import Dict, List

COINS: List[int] = [50, 25, 10, 5, 2, 1]  # already descending


def find_coins_greedy(amount: int) -> Dict[int, int]:
    """Greedy: pick the largest coin possible each step."""
    if amount <= 0:
        return {}

    res: Dict[int, int] = {}
    remaining = amount

    for coin in COINS:  # no need to sort каждый раз
        if remaining == 0:
            break
        cnt = remaining // coin
        if cnt:
            res[coin] = cnt
            remaining -= cnt * coin

    return res


def find_min_coins(amount: int) -> Dict[int, int]:
    """
    DP: minimum number of coins for 'amount'.
    Optimization: store only dp[s] + last_coin[s], reconstruct at the end.
    """
    if amount <= 0:
        return {}

    INF = amount + 1
    dp = [0] + [INF] * amount
    last_coin = [0] * (amount + 1)

    for s in range(1, amount + 1):
        best = INF
        chosen = 0
        for coin in COINS:
            if coin <= s:
                cand = dp[s - coin] + 1
                if cand < best:
                    best = cand
                    chosen = coin
        dp[s] = best
        last_coin[s] = chosen

    if dp[amount] == INF:  # theoretically unreachable with coin=1, but keep safe
        return {}

    # reconstruct
    res: Dict[int, int] = {}
    s = amount
    while s > 0:
        coin = last_coin[s]
        res[coin] = res.get(coin, 0) + 1
        s -= coin

    # optional: make output pretty (ascending keys)
    return dict(sorted(res.items()))


def compare_algorithms(test_amounts: List[int]) -> None:
    print("ALGORITHM COMPARISON")
    print(f"{'Amount':<8} {'Greedy(ms)':<12} {'DP(ms)':<12} {'Coins Greedy':<12} {'Coins DP'}")

    for amount in test_amounts:
        t0 = time.perf_counter()
        greedy_res = find_coins_greedy(amount)
        greedy_ms = (time.perf_counter() - t0) * 1000
        greedy_coins = sum(greedy_res.values())

        t0 = time.perf_counter()
        dp_res = find_min_coins(amount)
        dp_ms = (time.perf_counter() - t0) * 1000
        dp_coins = sum(dp_res.values())

        print(f"{amount:<8} {greedy_ms:<12.3f} {dp_ms:<12.3f} {greedy_coins:<12} {dp_coins}")


if __name__ == "__main__":
    amount = 113
    print("TEST FOR SUM 113")
    print("Greedy algorithm:", find_coins_greedy(amount))
    print("Dynamic programming:", find_min_coins(amount))
    print()

    test_amounts = [30, 113, 250, 1000, 5000, 10000]
    compare_algorithms(test_amounts)

    print("\nTIME COMPLEXITY:")
    print("Greedy: O(k) where k = number of coin types")
    print("DP:     O(amount * k)")
