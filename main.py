from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(lambda: 0)
        for num in nums1:
            d[num] += 1

        res = []
        for num in nums2:
            if num not in d:
                continue

            if d[num] > 0:
                res.append(num)
                d[num] -= 1

        return res


if __name__ == '__main__':
    a = Solution().intersect([1,2,2,1],[2,2])
    assert [2, 2] == a
    b = Solution().intersect([4,9,5],[9,4,9,8,4])
    assert [9,4] == b
