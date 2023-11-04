from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'Node(v={self.val}, next={self.next})'


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        root = head
        while root is not None:
            cur = root
            while cur.next and root.val == cur.next.val:
                cur = cur.next

            root.next = cur.next
            root = root.next

        return head


if __name__ == '__main__':
    c1 = ListNode(1, ListNode(1, ListNode(2)))
    print(Solution().deleteDuplicates(c1))

    c2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    print(Solution().deleteDuplicates(c2))
