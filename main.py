from typing import List


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[float('inf') for _ in range(n)] for _ in range(n)]
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: List[int]) -> None:
        f, t, w = edge
        self.graph[f][t] = w

    def shortestPath(self, node1: int, node2: int) -> int:
        start, end = node1, node2

        dest = [float('inf') for _ in range(len(self.graph))]
        dest[start] = 0

        visited = {start}
        cur = start
        while len(visited) != len(self.graph):
            m = None
            for i in range(len(self.graph)):
                if i in visited:
                    continue

                if dest[i] > dest[cur] + self.graph[cur][i]:
                    dest[i] = dest[cur] + self.graph[cur][i]

                if m is None or dest[m] > dest[i]:
                    m = i

            visited.add(cur)

            if cur == end:
                return dest[end] if dest[end] != float('inf') else -1

            cur = m

        return -1


if __name__ == '__main__':
    g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
    print(g.shortestPath(3, 2))
    print(g.shortestPath(0, 3))
    g.addEdge([1, 3, 4])
    print(g.shortestPath(0, 3))
