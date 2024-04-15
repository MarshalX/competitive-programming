from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node: TreeNode, num: int, storage: List[int], left: bool):
        res = 0
        if node.left: res += self.dfs(node.left, num, storage, True)
        if node.right: res += self.dfs(node.right, num, storage, False)
        if left and not node.left and not node.right: num += node.val; return num
        return res

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0, [], False)


if __name__ == '__main__':
    a = Solution().sumOfLeftLeaves(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
    assert 24 == a
    a = Solution().sumOfLeftLeaves(TreeNode(1))
    assert 0 == a
