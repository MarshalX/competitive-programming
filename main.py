from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific_water_flow, atlantic_water_flow = set(), set()

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    pacific_water_flow.add((i, j))
                if i == m - 1 or j == n - 1:
                    atlantic_water_flow.add((i, j))

        row_offset_matrix, col_offset_matrix = [-1, 1, 0, 0], [0, 0, -1, 1]

        def visit_inner() -> bool:
            changed = False

            for i in range(m):
                for j in range(n):
                    for ocean in [pacific_water_flow, atlantic_water_flow]:
                        if (i, j) in ocean:
                            continue

                        for shift_index in range(4):
                            ni = i + row_offset_matrix[shift_index]
                            nj = j + col_offset_matrix[shift_index]

                            if (ni, nj) in ocean and heights[i][j] >= heights[ni][nj]:
                                ocean.add((i, j))
                                changed = True

            return changed

        while visit_inner(): pass

        return [[x, y] for (x, y) in pacific_water_flow.intersection(atlantic_water_flow)]


if __name__ == '__main__':
    assert sorted([[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]) == sorted(Solution().pacificAtlantic([[1,2,3],[8,9,4],[7,6,5]]))
    assert sorted([[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]) == sorted(Solution().pacificAtlantic([[10,10,10],[10,1,10],[10,10,10]]))
    assert [[0,1],[1,0],[1,1]] == Solution().pacificAtlantic([[1,2],[4,3]])
    Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
