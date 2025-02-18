from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res_og = nums[0]
        res = abs(0 - nums[0])
        for n in nums:
            d = abs(0 - n)
            if d < res:
                res = d
                res_og = n
            elif d == res:
                res_og = max(res_og, n)

        return res_og


if __name__ == '__main__':
    a = Solution().findClosestNumber([-4,-2,1,4,8])
    assert a == 1
    a = Solution().findClosestNumber([2,-1,1])
    assert a == 1
