class Solution:
    def findMin(self, a: List[int]) -> int:
        ans=float('inf')
        l,h=0,len(a)-1
        while l<=h:
            m=l+(h-l)//2
            if a[l]<=a[m]:
                ans=min(ans,a[l])
                l=m+1
            else:
                ans=min(ans,a[m])
                h=m-1
        return ans