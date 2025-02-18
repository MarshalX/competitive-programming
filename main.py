from collections import defaultdict


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = defaultdict(int)
        for stone in stones:
            c[stone] += 1

        res = 0
        for jewel in jewels:
            res += c[jewel]

        return res
