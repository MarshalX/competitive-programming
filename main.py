import math


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c, ll = 0, head
        while ll:
            c += 1
            ll = ll.next

        m = int(math.ceil((c + 0.5) / 2))

        c, ll = 0, head
        while ll:
            c += 1
            if c == m:
                return ll
            ll = ll.next
