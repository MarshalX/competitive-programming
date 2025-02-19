from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []

        l, r = 0, len(nums) - 1
        while l <= r:
            lsqr = nums[l]**2
            rsqr = nums[r]**2

            if rsqr >= lsqr:
                res.append(rsqr)
                r -= 1
            else:
                res.append(lsqr)
                l += 1

        return res[::-1]
