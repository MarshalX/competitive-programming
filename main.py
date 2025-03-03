from typing import List
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = {i: set() for i in range(n)}
        for time in times:
            start, stop, weight = time
            g[start - 1].add((weight, stop - 1))

        dist = {n: float('inf') for n in g.keys()}
        dist[k - 1] = 0

        visited = set()
        priority_queue = [(0, k - 1)]
        while priority_queue:
            cur_weight, cur_node = heapq.heappop(priority_queue)
            visited.add(cur_node)

            if cur_weight > dist[cur_node]:
                continue

            for neighborhood_weight, neighborhood in g[cur_node]:
                if neighborhood in visited:
                    continue

                new_dist = cur_weight + neighborhood_weight
                if new_dist < dist[neighborhood]:
                    dist[neighborhood] = new_dist

                heapq.heappush(priority_queue, (new_dist, neighborhood))

        return max(dist.values()) if len(visited) == n else -1


if __name__ == '__main__':
    print(Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
    print(Solution().networkDelayTime(times = [[1,2,1]], n = 2, k = 2))
