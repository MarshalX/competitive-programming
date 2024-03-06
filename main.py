from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        res = []

        i1 = i2 = 0
        while i1 != m:
            if i2 >= n:
                res.append(nums1[i1])
                i1 += 1
            elif nums1[i1] < nums2[i2]:
                res.append(nums1[i1])
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                res.append(nums2[i2])
                i2 += 1
            else:
                res.append(nums2[i2])
                res.append(nums2[i2])
                i1 += 1
                i2 += 1

        while i2 != n:
            res.append(nums2[i2])
            i2 += 1

        for i in range(m + n):
            nums1[i] = res[i]


if __name__ == '__main__':
    a = [1, 2, 3, 0, 0, 0]
    Solution().merge(a, 3, [2, 5, 6], 3)
    assert [1, 2, 2, 3, 5, 6] == a
