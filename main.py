class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {0: 1, 1: 2}

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n - 1]


if __name__ == '__main__':
    print(Solution().climbStairs(1))
    print(Solution().climbStairs(2))
    print(Solution().climbStairs(3))
