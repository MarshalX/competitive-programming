from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs)

        d = defaultdict(lambda: [])
        for pair in adjacentPairs:
            u, v = pair
            d[u].append(v)
            d[v].append(u)

        start = None
        for k, v in d.items():
            if len(v) == 1:
                start = k
                break

        res = [start]

        cur = start
        prev = None
        for _ in range(n):
            if len(d[cur]) < 2:
                p = d[cur][0]
            else:
                p1, p2 = d[cur]
                p = p1 if p1 != prev else p2

            prev = cur
            cur = p

            res.append(p)

        return res


if __name__ == '__main__':
    cases = [
        [[2, 1], [3, 4], [3, 2]],
        [[4, -2], [1, 4], [-3, 1]],
        [[100000, -100000]],
    ]
    for case in cases:
        print(Solution().restoreArray(case))
