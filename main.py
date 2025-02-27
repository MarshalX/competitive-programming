from collections import defaultdict
from typing import List



class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d = defaultdict(list)
        for (f, t) in edges:
            d[f].append(t)
            d[t].append(f)

        q = [source]
        visited = {source,}
        while q:
            t = q.pop(0)

            if t == destination:
                return True

            for e in d[t]:
                if e not in visited:
                    q.append(e)
                    visited.add(e)

        return False
