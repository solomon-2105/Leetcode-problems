class Solution:
    def combinationSum2(self, a: List[int], t: int) -> List[List[int]]:
        def brr(i,a,c,d,t):
            if t==0:
                d.append(c.copy())
                return
            if i==len(a) or t<0:
                return
            c.append(a[i])
            brr(i+1,a,c,d,t-a[i])
            c.pop()
            while i+1<len(a) and a[i]==a[i+1]:
                i+=1
            brr(i+1,a,c,d,t)
        a.sort()
        c,d=[],[]
        brr(0,a,c,d,t)
        return d