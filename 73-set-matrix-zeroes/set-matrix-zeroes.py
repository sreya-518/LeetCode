class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #row = matrix[0][..]
        #col = matrix[..][0]
        m = len(matrix)
        n = len(matrix[0])
        row1 = 1
    
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0]= 0
                    if j!=0:
                        matrix[0][j] = 0
                    else: 
                        row1=0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != 0:
                    if matrix[i][0] == 0 or matrix[0][j] ==0:
                        matrix[i][j]=0
        
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j]=0
        if row1 == 0:
            for i in range(m):
                matrix[i][0] = 0

        return matrix