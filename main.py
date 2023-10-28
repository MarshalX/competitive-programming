class Solution:
    def fib(self, n: int) -> int:
        dp = {0: 0, 1: 1}

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


if __name__ == '__main__':
    cases = [
        2,
        3,
        4,
        10,
        11,
        60
    ]

    for case in cases:
        print(Solution().fib(case))
