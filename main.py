from typing import List


class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        s = sum(nums[:k])
        l = sum(nums[-k:])
        return abs(s - l)
