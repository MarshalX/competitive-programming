from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node({self.val=}, {self.left=}, {self.right=})'


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if root is None:
            return res

        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                res.append(node.val)
            else:
                if node.left:
                    stack.append((node.left, False))

                if node.right:
                    stack.append((node.right, False))

                stack.append((node, True))

        return res[::-1]


if __name__ == '__main__':
    pass
