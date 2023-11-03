class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def _(r):
            if r is None:
                return []

            _(r.left)
            res.append(r.val)
            _(r.right)

        _(root)

        return res


if __name__ == '__main__':
    pass
