class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.' for j in range(n)] for i in range(n)]
        column=set()
        majorDiag=set()
        minorDiag=set()

        def isSafe(r,c):
            if c in column:
                return False
            if c-r in majorDiag:
                return False
            if c+r in minorDiag:
                return False
            return True
        
        def placeQueen(r,c):
            column.add(c)
            majorDiag.add(c-r)
            minorDiag.add(c+r)
            board[r][c]='Q'
        
        def removeQueen(r,c):
            column.remove(c)
            majorDiag.remove(c-r)
            minorDiag.remove(c+r)
            board[r][c]='.'
            
        def getString(arr):
            s=""
            for i in range(len(arr)):
                s=s+arr[i]
            
            return s
        
        ans=[]
        def solve(r):
            if r==n:
                solvedBoard=[]
                for row in board:
                    solvedBoard.append(getString(row))
                
                ans.append(solvedBoard)
                return
            
            for c in range(n):
                if isSafe(r,c):
                    placeQueen(r,c)
                    solve(r+1)
                    removeQueen(r,c)

        solve(0)
        return ans
