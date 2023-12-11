from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if nums[i] in dp:
                return [i, dp[nums[i]]]
            dp[t] = i


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum([3, 2, 4], 6))
    print(Solution().twoSum([3, 3], 6))
