from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node: TreeNode, num: int, storage: List[int]):
        if node.left: self.dfs(node.left, num * 10 + node.val, storage)
        if node.right: self.dfs(node.right, num * 10 + node.val, storage)
        if not node.left and not node.right: storage.append(num * 10 + node.val)
        return storage

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return sum(self.dfs(root, 0, []))


if __name__ == '__main__':
    a = Solution().sumNumbers(TreeNode(1))
    assert 1 == a
    a = Solution().sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3)))
    assert 25 == a
    a = Solution().sumNumbers(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0)))
    assert 1026 == a
