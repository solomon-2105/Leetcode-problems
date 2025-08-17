class Solution:
    def searchMatrix(self, a: List[List[int]], t: int) -> bool:
        row,col=0,len(a[0])-1
        while row<len(a) and col>=0:
            if a[row][col]==t:
                return True
            elif a[row][col]<t:
                row+=1
            else:
                col-=1
        return False