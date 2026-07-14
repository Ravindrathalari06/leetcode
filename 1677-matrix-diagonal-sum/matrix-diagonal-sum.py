class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        s=0
        for i in range(n):
            s+=mat[i][i]
            if i!=n-i-1:
                s+=mat[i][n-i-1]
        return s
        