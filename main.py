class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def _(r):
            if r is None:
                return []

            _(r.left)
            _(r.right)
            res.append(r.val)

        _(root)

        return res


if __name__ == '__main__':
    pass
