from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        p1, p2 = 0, 0
        for i in range(len(nums)):
            while p1 < len(nums) and nums[p1] & 1 != 1:
                p1 += 1
            while p2 < len(nums) and nums[p2] & 1 == 1:
                p2 += 1

            if i & 1 == 1 and nums[i] & 1 != 1:
                nums[i], nums[p1] = nums[p1], nums[i]
            elif i & 1 != 1 and nums[i] & 1 == 1:
                nums[i], nums[p2] = nums[p2], nums[i]

            if p1 < i:
                p1 = i + 1
            if p2 < i:
                p2 = i + 1

        return nums


if __name__ == '__main__':
    a = Solution().sortArrayByParityII([3, 4])
    assert [4, 3] == a
    a = Solution().sortArrayByParityII([4, 1, 1, 4])
    assert [4, 1, 4, 1] == a
    a = Solution().sortArrayByParityII([4, 1, 2, 1])
    assert [4, 1, 2, 1] == a
    a = Solution().sortArrayByParityII([2, 3])
    assert [2, 3] == a
    a = Solution().sortArrayByParityII([1, 1, 1, 1, 2, 2, 2, 2])
    assert [2, 1, 2, 1, 2, 1, 2, 1] == a
    a = Solution().sortArrayByParityII([2, 2, 2, 2, 1, 1, 1, 1])
    assert [2, 1, 2, 1, 2, 1, 2, 1] == a
    a = Solution().sortArrayByParityII([2, 2, 2, 2, 2, 1, 1, 1, 1, 1])
    assert [2, 1, 2, 1, 2, 1, 2, 1, 2, 1] == a
