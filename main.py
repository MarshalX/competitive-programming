from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned_root_node = Node(node.val)
        created_nodes = {node.val: cloned_root_node}

        queue = [(cloned_root_node, node)]
        visited = {node.val,}
        while queue:
            cloned_node, real_node = queue.pop(0)
            for neighbor in real_node.neighbors:
                if neighbor.val in created_nodes:
                    neighbor_cloned_node = created_nodes[neighbor.val]
                else:
                    neighbor_cloned_node = Node(neighbor.val)
                    created_nodes[neighbor.val] = neighbor_cloned_node

                cloned_node.neighbors.append(neighbor_cloned_node)

                if neighbor.val not in visited:
                    queue.append((neighbor_cloned_node, neighbor))
                    visited.add(neighbor.val)

        return cloned_root_node
