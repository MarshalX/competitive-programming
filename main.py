from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        dp = [0] * len(prices)
        dp[0] = prices[1] - prices[0]
        min_price = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return max(0, dp[-1])


if __name__ == '__main__':
    assert 1 == Solution().maxProfit([1, 2])
    assert 3 == Solution().maxProfit([1, 2, 4])
    assert 5 == Solution().maxProfit([7,1,3,5,6,4])
    assert 0 == Solution().maxProfit([7,6,4,3,1])
