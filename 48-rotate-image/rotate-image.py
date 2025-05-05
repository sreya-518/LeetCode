class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        #Transpose
        for i in range(0, n-1):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        #reverse row's
        #for i in range(n):
        #    matrix[i] = matrix[i][::-1]

        for i in range(n):
            p1 = 0
            pn = n-1
            while p1<pn:
                matrix[i][p1], matrix[i][pn] = matrix[i][pn], matrix[i][p1]
                p1 +=1
                pn -=1