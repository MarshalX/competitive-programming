class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def _(r, d) -> int:
            if r is None:
                return d

            l = _(r.left, d + 1)
            r = _(r.right, d + 1)

            return max(l, r)

        return _(root, 0)


if __name__ == '__main__':
    print(Solution().maxDepth(None))
