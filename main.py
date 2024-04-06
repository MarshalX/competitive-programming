from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[i ^ 1 for i in reversed(r)] for r in image]


if __name__ == '__main__':
    a = Solution().flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]])
    assert [[1, 0, 0], [0, 1, 0], [1, 1, 1]] == a
    a = Solution().flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]])
    assert [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]] == a
