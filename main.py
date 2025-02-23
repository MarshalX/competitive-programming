from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def _(node: Optional[TreeNode], curSum: int = 0):
            if not node:
                return False

            curSum += node.val
            if not node.left and not node.right:
                return targetSum == curSum

            return _(node.left, curSum) or _(node.right, curSum)

        return _(root)


if __name__ == '__main__':
    assert True == Solution().hasPathSum(
        TreeNode(4,
            TreeNode(2,
                TreeNode(1),
                TreeNode(3)
             ),
            TreeNode(7,
                TreeNode(6),
                TreeNode(9)
             )
        ),
        targetSum=9
    )
