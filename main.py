import queue
from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        qe = queue.Queue()

        qe.put(p)
        qe.put(q)
        while not qe.empty():
            n1 = qe.get()
            n2 = qe.get()

            if n1 is None or n2 is None:
                if n1 != n2:
                    return False
                continue

            if n1.val != n2.val:
                return False

            qe.put(n1.left)
            qe.put(n1.right)
            qe.put(n2.left)
            qe.put(n2.right)

        return True


if __name__ == '__main__':
    pass
