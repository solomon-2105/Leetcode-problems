class Solution:
    def combinationSum(self, a: List[int], t: int) -> List[List[int]]:
        def brr(i,a,c,d,t):
            if i==len(a):
                if t==0:
                    d.append(c.copy())
                return
            if a[i]<=t:
                c.append(a[i])
                brr(i,a,c,d,t-a[i])
                c.pop()
            brr(i+1,a,c,d,t)

        c,d=[],[]
        brr(0,a,c,d,t)
        return d