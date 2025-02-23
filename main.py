from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


if __name__ == '__main__':
    Solution().invertTree(
        TreeNode(4,
            TreeNode(2,
                TreeNode(1),
                TreeNode(3)
             ),
            TreeNode(7,
                TreeNode(6),
                TreeNode(9)
             )
        )
    )
