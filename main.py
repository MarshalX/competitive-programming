class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        for y in range(m):
            dp[(n - 1, y)] = 1
        for x in range(n):
            dp[(x, m - 1)] = 1

        for x in reversed(range(n - 1)):
            for y in reversed(range(m - 1)):
                dp[(x, y)] = dp[(x + 1, y)] + dp[x, y + 1]

        return dp[(0, 0)]


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 7))
    print(Solution().uniquePaths(3, 2))
