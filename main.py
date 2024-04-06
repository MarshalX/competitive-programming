from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        last = 0
        for i in range(len(nums)):
            if nums[i] & 1 != 1:
                tmp = nums[last]
                nums[last] = nums[i]
                nums[i] = tmp
                last += 1

        return nums


if __name__ == '__main__':
    a = Solution().sortArrayByParity([3, 1, 2, 4])
    assert [2, 4, 3, 1] == a
    a = Solution().sortArrayByParity([0])
    assert [0] == a
