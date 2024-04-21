class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA=headA
        currB=headB
        flag1=False
        flag2=False
        while currA!=currB:
            currA=currA.next
            if currA is None and flag1 is False:
                flag1=True
                currA=headB
            
            currB=currB.next
            if currB is None and flag2 is False:
                flag2=True
                currB=headA
            
        return currA
