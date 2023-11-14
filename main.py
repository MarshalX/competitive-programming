import heapq
from typing import List


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[float('inf')] * n for _ in range(n)]
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: List[int]) -> None:
        f, t, w = edge
        self.graph[f][t] = w

    def shortestPath(self, node1: int, node2: int) -> int:
        start, end = node1, node2

        dest = [float('inf')] * len(self.graph)
        dest[start] = 0

        q = []
        heapq.heappush(q, (0, start))
        while q:
            cur_cost, cur = heapq.heappop(q)

            if cur_cost > dest[cur]:
                continue

            if cur == end:
                return cur_cost

            for i, cost in enumerate(self.graph[cur]):
                if cost == float('inf'):
                    continue

                if dest[i] > dest[cur] + cost:
                    dest[i] = dest[cur] + cost
                    heapq.heappush(q, (dest[i], i))

        return dest[end] if dest[end] != float('inf') else -1


if __name__ == '__main__':
    g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
    print(g.shortestPath(3, 2))
    print(g.shortestPath(0, 3))
    g.addEdge([1, 3, 4])
    print(g.shortestPath(0, 3))
