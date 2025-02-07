from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        max_x, min_y = len(grid[0]), 0
        x, y = 0, len(grid) - 1

        res = 0
        while y >= min_y and x < max_x:
            if grid[y][x] < 0:
                res += max_x - x
                y -= 1
            else:
                x += 1

        return res


if __name__ == '__main__':
    a = Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
    assert a == 8
    a = Solution().countNegatives([[3,2],[1,0]])
    assert a == 0
