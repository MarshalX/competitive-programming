class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        slow = head.next
        if slow is None:
            return None

        fast = head.next.next

        while slow != fast:
            slow = slow.next

            if slow is None or (fast is None or fast.next is None):
                return None

            fast = fast.next.next

        cycle_start = head
        while head != fast:
            head = head.next
            fast = fast.next
            cycle_start = head

        return cycle_start


if __name__ == '__main__':
    pass
