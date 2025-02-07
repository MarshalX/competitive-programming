from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)


if __name__ == '__main__':
    print(Solution().findMin([0]))
    print(Solution().findMin([2, 1]))
    print(Solution().findMin([2, 3, 1]))
    print(Solution().findMin([2,3,4,5,1]))
    print(Solution().findMin([5,1,2,3,4]))
    print(Solution().findMin([3,4,5,6,1,2]))

    a = Solution().findMin([3,4,5,1,2])
    assert 1 == a
    a = Solution().findMin([4,5,6,7,0,1,2])
    assert 0 == a
    a = Solution().findMin([11,13,15,17])
    assert 11 == a
