class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS,COLS=len(matrix),len(matrix[0])
        r,c=0,0
        res=[]
        while ROWS>1 and COLS>1:

            for k in range(COLS-1):
                res.append(matrix[r][c])
                c+=1
            
            for k in range(ROWS-1):
                res.append(matrix[r][c])
                r+=1
            
            for k in range(COLS-1):
                res.append(matrix[r][c])
                c-=1
            
            for k in range(ROWS-1):
                res.append(matrix[r][c])
                r-=1
            
            ROWS-=2
            COLS-=2
            r+=1
            c+=1
        
        if COLS==0 or ROWS==0:
            return res
        
        if ROWS>COLS:
            for k in range(ROWS):
                res.append(matrix[r][c])
                r+=1
        else:
            for k in range(COLS):
                res.append(matrix[r][c])
                c+=1
        
        return res
