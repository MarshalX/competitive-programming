from typing import List


class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        return [n for _, n in sorted([(int(bin(n)[2::][::-1], 2), n) for n in sorted(nums)], key=lambda n: n[0])]
