class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        walls_set={(x, y)for x,y in walls}
        guards_set={(x, y)for x,y in guards}
        matrix=[[0 for _ in range(n)]for _ in range(m)]
        for x,y in walls_set:
            matrix[x][y]='W'
        for x,y in guards_set:
            matrix[x][y]='G'
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='G':
                    self.checkLeft(matrix,i,j)
                    self.checkRight(matrix,i,j,n)
                    self.checkUp(matrix,i,j)
                    self.checkDown(matrix,i,j,m)
        count=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0: count+=1
        return count

    
    def checkLeft(self,matrix,i,j):
        for k in range(j-1,-1,-1):
            if matrix[i][k]=='W' or matrix[i][k]=='G':
                return
            else:
                matrix[i][k]=-1
        return


    def checkRight(self,matrix,i,j,n):
        for k in range(j+1,n):
            if matrix[i][k]=='W' or matrix[i][k]=='G':
                return
            else:
                matrix[i][k]=-1
        return

    def checkUp(self,matrix,i,j):
        for k in range(i-1,-1,-1):
            if matrix[k][j]=='W' or matrix[k][j]=='G':
                return
            else:
                matrix[k][j]=-1
        return

    def checkDown(self,matrix,i,j,m):
        for k in range(i+1,m):
            if matrix[k][j]=='W' or matrix[k][j]=='G':
                return
            else:
                matrix[k][j]=-1
        return