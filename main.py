from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        count = max_count = 1
        prev = res = nums[0]
        for n in range(1, len(nums)):
            if nums[n] != prev:
                count = 1
                prev = nums[n]
                continue

            count += 1
            if max_count < count:
                max_count = count
                res = nums[n]

        return res


if __name__ == '__main__':
    print(Solution().majorityElement([1]))
    print(Solution().majorityElement([3, 2, 3]))
    print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
    print(Solution().majorityElement([3, 3, 4]))
