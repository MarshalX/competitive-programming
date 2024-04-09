from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)
        if s % 3 != 0:
            return False

        e = s // 3
        c, p = None, 0
        for n in arr:
            if c == e:
                p += 1
                if p == 3:
                    break
                c = 0

            c = (c or 0) + n

        if c == e:
            p += 1

        return min(3, p) == 3 and c in {0, e}


if __name__ == '__main__':
    a = Solution().canThreePartsEqualSum([1, -1, 1, -1])
    assert False is a
    a = Solution().canThreePartsEqualSum([0, 0, 0, 0])
    assert True is a
    a = Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1])
    assert True is a
    a = Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1])
    assert False is a
    a = Solution().canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4])
    assert True is a
