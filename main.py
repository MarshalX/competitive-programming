from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        def calc(pp1, pp2):
            nonlocal res
            m = min(height[pp1], height[pp2])
            if m != 0:
                for i in range(pp1, pp2):
                    d = m - height[i]
                    if d < 0:
                        continue

                    res += d

        o1, ho = 0, 0
        for i, h in enumerate(height):
            if h > ho:
                calc(o1, i)
                o1, ho = i, h

        o2, ho = len(height) - 1, 0
        for i, h in enumerate(reversed(height)):
            if h > ho:
                calc(len(height) - 1 - i, o2)
                o2, ho = len(height) - 1 - i, h

        calc(o1, o2)
        return res


if __name__ == '__main__':
    a = Solution().trap(height=[0, 1, 2, 0, 3, 0, 1, 2, 0, 0, 4, 2, 1, 2, 5, 0, 1, 2, 0, 2])
    assert 26 == a
    a = Solution().trap(height=[6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3])
    assert 83 == a
    a = Solution().trap(height=[5, 5, 1, 7, 1, 1, 5, 2, 7, 6])
    assert 23 == a
    a = Solution().trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    assert 6 == a
    a = Solution().trap(height=[3, 2, 4])
    assert 1 == a
    a = Solution().trap(height=[4, 2, 3])
    assert 1 == a
    a = Solution().trap(height=[9, 0, 0, 9])
    assert 18 == a
    a = Solution().trap(height=[4, 2, 0, 3, 2, 5])
    assert 9 == a
