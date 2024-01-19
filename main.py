from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dm = {v: i for i, v in enumerate(order)}
        wo = [[dm[c] for c in w] for w in words]
        wa = sorted(wo)
        return wo == wa


if __name__ == '__main__':
    print(Solution().isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
    print(Solution().isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
    print(Solution().isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))
    print(Solution().isAlienSorted(["kuvp", "q"], "ngxlkthsjuoqcpavbfdermiywz"))
