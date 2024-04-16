class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def reverse(node):
            if node is None or node.next is None:
                return node
            h=None
            curr=node

            while(curr is not None):
                temp=curr
                curr=curr.next
                temp.next=h
                h=temp

            return h
        
        def getFirstMid(node):
            slow=node
            fast=node

            while (fast is not None) and (fast.next is not None) and (fast.next.next is not None):
                slow=slow.next
                fast=fast.next.next
            
            return slow

        midNode=getFirstMid(head)
        midNext=midNode.next

        midNode.next=None
        hdash=reverse(midNext)

        curr1=head
        curr2=hdash

        while(curr1 is not None and curr2 is not None):
            if curr1.val!=curr2.val:
                return False
            curr1=curr1.next
            curr2=curr2.next

        return True
