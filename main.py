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

        if not root.left and not root.right:
            return targetSum == root.val

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


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
