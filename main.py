from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited = set()
        islands = {}

        m, n = len(grid), len(grid[0])

        def solve(x, y, island_id: int):
            if x < 0 or y < 0 or x > m - 1 or y > n - 1 or grid[x][y] == 0:
                return True

            if (x, y) in visited:
                return True

            visited.add((x, y))

            if islands[island_id] is not False:
                islands[island_id] += 1

            solve(x + 1, y, island_id)
            solve(x - 1, y, island_id)
            solve(x, y + 1, island_id)
            solve(x, y - 1, island_id)

            if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                islands[island_id] = False
                return False

        island_id = 0
        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if (x, y) not in visited and cell == 1:
                    islands[island_id] = 0
                    solve(x, y, island_id)
                    island_id += 1

        return sum([cells for cells in islands.values() if cells])


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
