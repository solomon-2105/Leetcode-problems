class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m , n = len(mat) , len(mat[0])
        row1 = [0] * m
        col1 = [0] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row1[i] += 1
                    col1[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row1[i] == 1 and col1[j] == 1:
                    ans += 1
        return ans