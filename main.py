from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num

        for i in range(len(nums) + 1):
            res ^= i

        return res


if __name__ == '__main__':
    print(Solution().missingNumber([3, 0, 1]))
    print(Solution().missingNumber([0, 1]))
    print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
