# HW-9 — Greedy Algorithms & Dynamic Programming
## Coin Change Problem

## Description

This homework compares two approaches for solving the coin change problem:

- Greedy algorithm
- Dynamic programming algorithm

We simulate a cash register system that gives change using a fixed set of coin denominations.

Coin denominations used in the task:

    COINS = [50, 25, 10, 5, 2, 1]

For a given amount, the system determines how many coins of each denomination should be used.

---

## Task Requirements

1. Implement a greedy algorithm `find_coins_greedy`:
   - Always selects the largest possible coin first
   - Returns `{coin: count}`

2. Implement a dynamic programming algorithm `find_min_coins`:
   - Finds the minimum number of coins
   - Returns `{coin: count}`

3. Compare both algorithms by:
   - Execution time
   - Big-O complexity
   - Performance on large amounts

---

## Greedy Algorithm

The greedy algorithm always takes the largest coin that fits into the remaining amount.

Example for amount 113:

    {50: 2, 10: 1, 2: 1, 1: 1}

Time complexity: `O(k)`  
Space complexity: `O(1)`

---

## Dynamic Programming Algorithm

The dynamic programming algorithm computes the minimum number of coins for all sums from 1 to the target amount and then reconstructs the solution.

Example for amount 113:

    {1: 1, 2: 1, 10: 1, 50: 2}

Time complexity: `O(amount × k)`  
Space complexity: `O(amount)`

---

## Program Output & Results

### Test for Sum = 113

    TEST FOR SUM 113
    Greedy algorithm: {50: 2, 10: 1, 2: 1, 1: 1}
    Dynamic programming: {1: 1, 2: 1, 10: 1, 50: 2}

Both algorithms return the same number of coins, only the order of denominations differs.

---

### Algorithm Comparison (Execution Time)

    ALGORITHM COMPARISON
    Amount   Greedy(ms)   DP(ms)       Coins Greedy   Coins DP
    30       0.002        0.013        2              2
    113      0.002        0.036        5              5
    250      0.002        0.082        5              5
    1000     0.001        0.339        20             20
    5000     0.002        1.639        100            100
    10000    0.001        3.172        200            200

The results show that:
- Greedy execution time remains almost constant
- Dynamic programming time increases linearly with the amount

---

## Time Complexity Summary

    Greedy: O(k) where k = number of coin types
    Dynamic Programming: O(amount × k)

---

## Conclusions

- For the coin set `[50, 25, 10, 5, 2, 1]`, the greedy algorithm is optimal and fastest.
- Dynamic programming guarantees the minimum number of coins but becomes slower for large amounts.
- In this task, greedy is the preferred solution, while dynamic programming serves as a universal fallback.

