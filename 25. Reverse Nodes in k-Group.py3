class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return self.reverseKGroupHelper(head,k)
    
    def reverseKGroupHelper(self,head,k):
        if head is None or head.next is None or k<2:
            return head
        
        h=None
        curr=head
        count=0

        while curr and count<k:
            temp=curr
            curr=curr.next
            temp.next=h
            h=temp
            count+=1
        
        if count<k:
            return self.reverseKGroupHelper(h,count)
        head.next=self.reverseKGroupHelper(curr,k)
        return h
