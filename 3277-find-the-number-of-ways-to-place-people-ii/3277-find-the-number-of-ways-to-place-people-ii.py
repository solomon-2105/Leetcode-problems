class Solution:
    def numberOfPairs(self, p: List[List[int]]) -> int:
        p.sort(key=lambda x:(x[0],-x[1]))  # sort by x asc, y desc
        n=len(p)
        count=0
        for i in range(n):
            c,d=p[i]
            for j in range(i+1,n):
                a,b=p[j]
                if d>=b:  # A must be upperleft of B
                    brr=True
                    for k in range(i+1,j):  # only check points in between
                        q,r=p[k]
                        if c<=q<=a and b<=r<=d:
                            brr=False
                            break
                    if brr:count+=1
        return count