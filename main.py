from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i = res = 0
        while tickets[k] != 0:
            if i == len(tickets):
                i = 0

            if tickets[i] != 0:
                tickets[i] -= 1
                res += 1

            i += 1

        return res


if __name__ == '__main__':
    a = Solution().timeRequiredToBuy(tickets=[2], k=0)
    assert 2 == a
    a = Solution().timeRequiredToBuy(tickets=[2, 3, 2], k=2)
    assert 6 == a
    a = Solution().timeRequiredToBuy(tickets=[5, 1, 1, 1], k=0)
    assert 8 == a
