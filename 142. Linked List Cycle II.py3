class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        
        if slow==fast:
            p1=head
            p2=slow

            while p1!=p2:
                p1=p1.next
                p2=p2.next
            return p1
        
        return None
