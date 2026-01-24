from typing import List, Tuple


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def solve(x, y) -> Tuple[int, bool]:
            if x < 0 or y < 0 or x >= m or y >= n:
                return 0, True
            if visited[x][y] or grid[x][y] == 0:
                return 0, False

            visited[x][y] = True

            size = 1
            invalid = x == 0 or x == m - 1 or y == 0 or y == n - 1

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                sub_size, sub_invalid = solve(x + dx, y + dy)
                size += sub_size
                invalid = invalid or sub_invalid

            return size, invalid

        result = 0
        for x in range(m):
            for y in range(n):
                if not visited[x][y] and grid[x][y] == 1:
                    size, invalid = solve(x, y)
                    if not invalid:
                        result += size

        return result


if __name__ == "__main__":
    grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    print(Solution().numEnclaves(grid))
    grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    print(Solution().numEnclaves(grid))
    grid = [
        [0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
        [1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
    ]
    print(Solution().numEnclaves(grid))
    grid = [
        [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1],
        [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    ]
    print(Solution().numEnclaves(grid))
