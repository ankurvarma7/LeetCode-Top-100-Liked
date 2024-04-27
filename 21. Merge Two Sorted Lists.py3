class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        h,t=None, None

        curr1=list1
        curr2=list2

        while curr1 and curr2:
            if curr1.val<=curr2.val:
                if h is None:
                    h=curr1
                    t=h
                
                else:
                    t.next=curr1
                    t=curr1
                
                curr1=curr1.next
            
            else:
                if h is None:
                    h=curr2
                    t=h
                
                else:
                    t.next=curr2
                    t=curr2
                
                curr2=curr2.next
            
        if curr1:
            t.next=curr1
            
        if curr2:
            t.next=curr2
            
        return h
