class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        cnt_max = 0
        index = 0 
        for i in range(n):
            cnt_ones = 0 
            for j in range(m):
                cnt_ones += mat[i][j]
            if cnt_ones > cnt_max:
                cnt_max = cnt_ones
                index = i
        return [index, cnt_max]
        