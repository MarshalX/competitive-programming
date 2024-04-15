from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bfs(self, node: TreeNode):
        res, q, visited = 0, [(node, False)], set()
        while q:
            i, l = q.pop()
            if not i or i in visited: continue

            if l and i.val and i.left is None and i.right is None: res += i.val
            visited.add(i)

            q.append((i.left, True))
            q.append((i.right, False))

        return res

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.bfs(root)


if __name__ == '__main__':
    a = Solution().sumOfLeftLeaves(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
    assert 24 == a
    a = Solution().sumOfLeftLeaves(TreeNode(1))
    assert 0 == a
