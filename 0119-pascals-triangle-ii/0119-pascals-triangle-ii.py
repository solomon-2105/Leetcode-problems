class Solution:
    def getRow(self, n: int) -> List[int]:
        a = []
        j = 1
        for i in range(n+1):
            b = [1]*j
            j+=1
            a.append(b)
        for i in range(2,n+1):
            for j in range(1,len(a[i])-1):
                a[i][j] = a[i-1][j] + a[i-1][j-1]
        return a[n]