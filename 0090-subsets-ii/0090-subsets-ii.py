class Solution:
    def subsetsWithDup(self, a: List[int]) -> List[List[int]]:
        a.sort()
        b,c=[],[]
        self.brr(a,0,b,c)
        return c
    
    def brr(self,a,i,b,c):
        if i==len(a):
            c.append(b.copy())
            return
        b.append(a[i])
        self.brr(a,i+1,b,c)
        b.pop()
        while i+1<len(a) and a[i]==a[i+1]:
            i+=1
        self.brr(a,i+1,b,c)       