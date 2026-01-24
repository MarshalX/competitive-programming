from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev_val, self.result = None, float("inf")

        def dfs(node):
            if node is None:
                return

            dfs(node.left)

            if self.prev_val is not None:
                self.result = min(self.result, node.val - self.prev_val)

            self.prev_val = node.val

            dfs(node.right)

        dfs(root)
        return self.result
