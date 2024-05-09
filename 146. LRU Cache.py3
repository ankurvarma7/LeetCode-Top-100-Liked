class ListNode:
    def __init__(self,key=0,value=0,next=None,prev=None):
        self.key=key
        self.value=value
        self.next=next
        self.prev=prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head=ListNode()
        self.tail=ListNode()
        self.head.next=self.tail
        self.tail.prev=self.head
        self.keyToNode={}

    def get(self, key: int) -> int:
        if key in self.keyToNode:
            node=self.keyToNode[key]
            self.deleteNode(node)
            self.insertNode(node)
            return node.value
        return -1
    def put(self, key: int, value: int) -> None:
        node=ListNode(key,value)
        if key in self.keyToNode:
            self.deleteNode(self.keyToNode[key])
            self.insertNode(node)
        else:
            if len(self.keyToNode)<self.capacity:
                self.insertNode(node)
            else:
                self.insertNode(node)
                self.keyToNode.pop(self.head.next.key)
                self.head.next=self.head.next.next
                self.head.next.prev=self.head
        
        self.keyToNode[key]=node
    
    def insertNode(self,node):
        node.prev=self.tail.prev
        self.tail.prev.next=node
        self.tail.prev=node
        node.next=self.tail
    
    def deleteNode(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        node.next=None
        node.prev=None
