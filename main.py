from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.unique_val = None

        def dfs(node: Optional[TreeNode]) -> bool:
            if node is None:
                return True

            if self.unique_val is None:
                self.unique_val = node.val
            elif self.unique_val != node.val:
                return False

            return dfs(node.left) and dfs(node.right)

        return dfs(root)
