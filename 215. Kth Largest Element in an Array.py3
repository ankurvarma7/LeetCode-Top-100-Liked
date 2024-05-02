class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap=[]
        heapq.heapify(minheap)

        for n in nums:
            if len(minheap)<k:
                heapq.heappush(minheap,n)
            
            else:
                if n>minheap[0]:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap,n)
        
        return minheap[0]
