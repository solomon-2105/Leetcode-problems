class Solution:
    def combinationSum2(self, a: List[int], t: int) -> List[List[int]]:
        a.sort()
        b,c=[],[]
        self.brr(a,0,b,t,c)
        return c
    
    def brr(self,a,i,b,k,c):
        if i==len(a):
            if k==0:
                c.append(b.copy())
            return
        if a[i]<=k:
            b.append(a[i])
            self.brr(a,i+1,b,k-a[i],c)
            b.pop()
        while i+1<len(a) and a[i]==a[i+1]:
            i+=1
        self.brr(a,i+1,b,k,c)