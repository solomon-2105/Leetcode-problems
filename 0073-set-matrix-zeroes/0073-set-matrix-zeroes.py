class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #bruteforce

        # def brr(ass,x,y):
        #     a=len(ass)
        #     b=len(ass[0])
        #     for j in range(b):
        #         if ass[x][j]!=0:  ass[x][j]="M"
        #     for i in range(a):
        #         if ass[i][y]!=0: ass[i][y]="M"
        # m=len(matrix)
        # n=len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j]==0:
        #             brr(matrix,i,j)
                
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j]=="M":
        #             matrix[i][j]=0
        
        #better
        # m=len(matrix)
        # n=len(matrix[0]) 
        # a=[0]*m
        # b=[0]*n
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j]==0:
        #             a[i]=b[j]=1       
        # for i in range(m):
        #     for j in range(n):
        #         if b[j]==1 or a[i]==1:
        #             matrix[i][j]=0

        #optimal anta
        m=len(matrix)
        n=len(matrix[0])
        col0=1
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    if j!=0: matrix[0][j]=0
                    else: col0=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]!=0:
                    if matrix[i][0]==0 or matrix[0][j]==0:
                        matrix[i][j]=0
        if matrix[0][0]==0:
            for j in range(n):
                matrix[0][j]=0
        if col0==0:
            for i in range(m):
                matrix[i][0]=0



















