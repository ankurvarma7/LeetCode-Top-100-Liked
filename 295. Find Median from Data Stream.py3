class MedianFinder:
    def __init__(self):
        self.minheap=[]
        self.maxheap=[]
        heapq.heapify(self.minheap)
        heapq.heapify(self.maxheap)

    def addNum(self, num: int) -> None:
        l1=len(self.minheap)
        l2=len(self.maxheap)

        if l1==0:
            heapq.heappush(self.minheap,num)
            l1+=1

        elif num>=self.minheap[0]:
            heapq.heappush(self.minheap,num)
            l1+=1

        else:
            heapq.heappush(self.maxheap,-1*num)
            l2+=1

        if l1-l2>1:
            temp=heapq.heappop(self.minheap)
            l1-=1
            heapq.heappush(self.maxheap,-1*temp)
            l2+=1

        if l2-l1>1:
            temp=heapq.heappop(self.maxheap)
            l2-=1
            heapq.heappush(self.minheap,-1*temp)
            l1+=1
       
    def findMedian(self) -> float:
        l1=len(self.minheap)
        l2=len(self.maxheap)

        if (l1+l2)%2==0:
            return (self.minheap[0]-self.maxheap[0])/2
        
        else:
            return self.minheap[0] if l1>l2 else self.maxheap[0]*-1
