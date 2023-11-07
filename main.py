from typing import Optional


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == val:
            return root

        if res := (self.searchBST(root.left, val) or self.searchBST(root.right, val)):
            return res

        return None


if __name__ == '__main__':
    pass
