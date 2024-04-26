class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
  
        coordinates=set()
        ROWS,COLS=len(matrix),len(matrix[0])
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j]==0:
                    coordinates.add((i,j))

        def setRowZero(r):
            for i in range(COLS):
                matrix[r][i]=0


        def setColZero(c):
            for i in range(ROWS):
                matrix[i][c]=0


        for r, c, in coordinates:
            setRowZero(r)
            setColZero(c)
