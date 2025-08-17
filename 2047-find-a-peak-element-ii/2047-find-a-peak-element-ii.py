class Solution:
    def findPeakGrid(self, a: List[List[int]]) -> List[int]:
        low,high=0,len(a[0])-1
        while low<=high:
            mid=low+(high-low)//2
            p,s=self.maxii(a,mid)
            if (s==0 or a[p][s]>a[p][s-1]) and (s==len(a[0])-1 or a[p][s]>a[p][s+1]):
                return [p,s]
            elif s>0 and a[p][s]<a[p][s-1]:
                high=mid-1
            else:
                low=mid+1
        return []
    def maxii(self,a,i):
        k,l=0,0
        vrr=float('-inf')
        for j in range(len(a)):
            if vrr<a[j][i]:
                vrr=a[j][i]
                k,l=j,i
        return [k,l]