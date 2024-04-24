class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftSmaller=[0]*len(heights)
        rightSmaller=[0]*len(heights)

        stack=[]

        def immediateSmallerLeft():
            leftSmaller[0]=-1
            stack.append(0)

            for i in range(1,len(heights)):
                if heights[stack[-1]]<heights[i]:
                    leftSmaller[i]=stack[-1]

                else:
                    while stack and heights[stack[-1]]>=heights[i]:
                        stack.pop()
                    
                    if stack:
                        leftSmaller[i]=stack[-1]
                    
                    else:
                        leftSmaller[i]=-1
                
                stack.append(i)
        

        

        def immediateSmallerRight():
            n=len(heights)
            rightSmaller[n-1]=n
            stack.append(n-1)

            for i in range(n-2,-1,-1):
                if heights[stack[-1]]<heights[i]:
                    rightSmaller[i]=stack[-1]

                else:
                    while stack and heights[stack[-1]]>=heights[i]:
                        stack.pop()
                    
                    if stack:
                        rightSmaller[i]=stack[-1]
                    
                    else:
                        rightSmaller[i]=n
                
                stack.append(i)
        
        immediateSmallerLeft()
        stack=[]
        immediateSmallerRight()
        ans=0
        
        for i in range(len(heights)):
            ans=max(ans,(heights[i]*(rightSmaller[i]-leftSmaller[i]-1)))
        
        return ans
