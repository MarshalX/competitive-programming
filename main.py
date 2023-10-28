from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if right == mid:
            return mid + 1

        return mid


if __name__ == '__main__':
    cases = [
        ([1, 3, 6], 5),
        ([1, 3, 5, 6], 5),
        ([1, 3, 5, 6], 2),
        ([1, 3, 5, 6], 7),
    ]

    for case in cases:
        print(Solution().searchInsert(case[0], case[1]))
