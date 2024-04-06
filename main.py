from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd, even = [], []
        for num in nums:
            odd.append(num) if num & 1 == 1 else even.append(num)
        return even + odd


if __name__ == '__main__':
    a = Solution().sortArrayByParity([3, 1, 2, 4])
    assert [2, 4, 3, 1] == a
    a = Solution().sortArrayByParity([0])
    assert [0] == a
