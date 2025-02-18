from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     known_nums = {}
     for i in range(len(nums)):
         diff = target - nums[i]
         if diff in known_nums:
             return [i, known_nums[diff]]
         known_nums[nums[i]] = i
