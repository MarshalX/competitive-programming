class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = head.next
        if slow is None:
            return False

        fast = head.next.next

        while slow != fast:
            slow = slow.next

            if slow is None or (fast is None or fast.next is None):
                return False

            fast = fast.next.next

        return True


if __name__ == '__main__':
    pass
