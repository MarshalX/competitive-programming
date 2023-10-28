from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}

        for i in range(1, amount + 1):
            for coin in coins:
                subproblem = i - coin
                if subproblem < 0 or coin > i:
                    continue

                cur_min = dp.get(i, float('INF'))
                prev_min = dp.get(subproblem, float('INF'))
                dp[i] = min(cur_min, prev_min + 1)

        res = dp.get(amount)
        if res == float('INF') or res is None:
            return -1

        return res


if __name__ == '__main__':
    cases = [
        ([5], 15),
        ([1, 2, 5], 11),
        ([2], 3),
        ([1], 0),
        ([470, 35, 120, 81, 121], 9825),
    ]

    for case in cases:
        print(Solution().coinChange(case[0], case[1]))
