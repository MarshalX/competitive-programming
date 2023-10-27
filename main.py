from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]

        return res


if __name__ == '__main__':
    cases = [
        [2, 2, 1],
        [4, 1, 2, 1, 2],
        [1],
    ]

    for case in cases:
        print(Solution().singleNumber(case))
