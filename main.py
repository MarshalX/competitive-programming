from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


if __name__ == '__main__':
    a = Solution().arrayPairSum([1, 1])
    assert 1 == a
    a = Solution().arrayPairSum([1, 4, 3, 2])
    assert 4 == a
    a = Solution().arrayPairSum([6, 2, 6, 5, 1, 2])
    assert 9 == a
