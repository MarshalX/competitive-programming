class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def _(r):
            if r is None:
                return []

            res.append(r.val)
            _(r.left)
            _(r.right)

        _(root)

        return res


if __name__ == '__main__':
    pass
