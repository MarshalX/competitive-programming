from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []

        for o in operations:
            try:
                o = int(o)
            except ValueError:
                pass

            if isinstance(o, int):
                s.append(o)
            elif o == '+':
                s.append(s[-1] + s[-2])
            elif o == 'D':
                s.append(2 * s[-1])
            elif o == 'C':
                s.pop()

        return sum(s)
