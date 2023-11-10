from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node({self.val=}, {self.left=}, {self.right=})'


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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

                stack.append((node, True))

                if node.right:
                    stack.append((node.right, False))

        return res[::-1]


if __name__ == '__main__':
    t = TreeNode(0, TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(4, TreeNode(5)))

    #             0
    #     1               4
    # 2       3       5

    # 2 1 3 0 5 4

    print(Solution().inorderTraversal(t))
