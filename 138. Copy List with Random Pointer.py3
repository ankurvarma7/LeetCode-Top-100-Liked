class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap={}
        nodeMap[None]=None
        h=None
        t=None
        curr=head

        while curr:
            node=Node(curr.val)
            nodeMap[curr]=node
            if h:
                t.next=node
                t=t.next
            else:
                h=node
                t=h
            
            curr=curr.next
        

        curr=head

        while curr:
            nodeMap[curr].random=nodeMap[curr.random]
            curr=curr.next
        
        return h
