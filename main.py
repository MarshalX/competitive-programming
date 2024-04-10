from typing import Iterable, List


class Solution:
    def simulate(self, n: int) -> Iterable[int]:
        sim = [i for i in range(n)]
        rev = []

        while sim:
            rev.append(sim[0])
            sim.pop(0)
            if len(sim) > 1:
                sim.append(sim[0])
                sim.pop(0)

        return rev

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        res = [0] * n
        it = iter(sorted(deck))
        for i in self.simulate(n):
            res[i] = next(it)

        return res


if __name__ == '__main__':
    a = Solution().deckRevealedIncreasing([17])
    assert [17] == a
    a = Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7])
    assert [2, 13, 3, 11, 5, 17, 7] == a
