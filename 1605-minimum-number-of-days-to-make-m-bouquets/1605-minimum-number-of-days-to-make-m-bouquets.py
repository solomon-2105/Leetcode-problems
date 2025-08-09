class Solution:
    def check(self,a,p,k,m):
        c=0
        s=0
        for val in a:
            if val<=p:
                s+=1
                if s==k:
                    c+=1
                    if c>=m:return c
                    s=0
            else:
                s=0
        return c

    def minDays(self,a:List[int],m:int,k:int)->int:
        if m*k>len(a):return -1
        low=min(a)
        high=max(a)
        ans=-1
        while low<=high:
            mid=low+(high-low)//2
            if self.check(a,mid,k,m)>=m:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
