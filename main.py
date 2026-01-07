from typing import List


class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda n: (int(bin(n)[2:][::-1]), n))
