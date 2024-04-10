from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sim, res = deque(range(len(deck))), [0] * len(deck)
        for card in sorted(deck):
            res[sim.popleft()] = card
            sim and sim.append(sim.popleft())
        return res


if __name__ == '__main__':
    a = Solution().deckRevealedIncreasing([17])
    assert [17] == a
    a = Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7])
    assert [2, 13, 3, 11, 5, 17, 7] == a
